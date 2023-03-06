#script to generate inputs to nci calculations of solids
#Sabrina Grigoletto - UFMG - Brazil

import os

fragment1 = ['system1', 'system2']
fragment2 = ['molec1', 'molec2', 'molec3', 'molec4', 'molec5', 'molec6', 'molec7', 'molec8']

main_dir = "nci_calculations"
os.mkdir(main_dir)

for i in range(len(fragment1)):
    for j in range(len(fragment2)):
        dir_name = f'nci_{fragment1[i]}_{fragment2[j]}'
        dir_path = os.path.join(main_dir, dir_name)
        os.makedirs(dir_path)
        file_path = os.path.join(dir_path, "input.cri")
        with open(file_path, "w") as file:
            file.write(f'CRYSTAL {fragment1[i]}_{fragment2[j]}.cube\n')
            file.write(f'LOAD {fragment1[i]}_{fragment2[j]}.cube CORE ZPSP Cu 19 N 5 C 4 Si 4 H 1 F 7\n') #set number of Z of pseudopotential
            file.write(f'LOAD {fragment1[i]}_{fragment2[j]}.cube\n')
            file.write('NCIPLOT\n')
            file.write(f'       fragment {fragment1[i]}.xyz\n')
            file.write(f'       fragment {fragment2[j]}.xyz\n')
            file.write('       NSTEP 400 400 400\n')
            file.write(f'       ONAME {fragment1[i]}_{fragment2[j]}\n')
            file.write('ENDNCIPLOT\n')
            file.write(f'WRITE {fragment1[i]}_{fragment2[j]}.cif')
