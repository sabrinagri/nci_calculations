#script to generate inputs to nci calculations of solids
#Sabrina Grigoletto - UFMG - Brazil

import os

mof = ['sifsix-2-cu', 'sifsix-2-i-cu']
molecule = ['methane', 'ethane', 'ethene', 'ethyne', 'propane', 'propene', 'propine', 'n2']

main_dir = "nci_calculations"
os.mkdir(main_dir)

for i in range(len(mof)):
    for j in range(len(molecule)):
        dir_name = f'nci_{mof[i]}_{molecule[j]}'
        dir_path = os.path.join(main_dir, dir_name)
        os.makedirs(dir_path)
        file_path = os.path.join(dir_path, "input.cri")
        with open(file_path, "w") as file:
            file.write(f'CRYSTAL {mof[i]}_{molecule[j]}.cube\n')
            file.write(f'LOAD {mof[i]}_{molecule[j]}.cube CORE ZPSP Cu 19 N 5 C 4 Si 4 H 1 F 7\n') #set number of Z os pseudopotential
            file.write(f'LOAD {mof[i]}_{molecule[j]}.cube\n')
            file.write('NCIPLOT\n')
            file.write(f'       fragment {mof[i]}.xyz\n')
            file.write(f'       fragment {molecule[j]}.xyz\n')
            file.write('       NSTEP 400 400 400\n')
            file.write(f'       ONAME {mof[i]}_{molecule[j]}\n')
            file.write('ENDNCIPLOT\n')
            file.write(f'WRITE {mof[i]}_{molecule[j]}.cif')
