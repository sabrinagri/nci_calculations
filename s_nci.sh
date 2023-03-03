#!/bin/bash

mof=(sifsix-2-cu sifsix-2-i-cu)
molecule=(methane ethane ethene ethyne propane propene propine n2)

for i in "${mof[@]}"
do
        for j in "${molecule[@]}"
        do
        cp script_critic2.sh ./nci_${i}_${j}
        chmod +x ./nci_${i}_${j}
        cd ./nci_${i}_${j}
        sh /script_critic2.sh input # add dir path
        cd ../
done
done
