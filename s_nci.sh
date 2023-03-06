#!/bin/bash

fragment1=(system1 system2)
fragment2=(molec1 molec2 molec3 molec4 molec5 molec6 molec7)

for i in "${fragment1[@]}"
do
        for j in "${fragment2[@]}"
        do
        cp script_critic2.sh ./nci_${i}_${j}
        chmod +x ./nci_${i}_${j}
        cd ./nci_${i}_${j}
        sh /script_critic2.sh input # add dir path
        cd ../
done
done
