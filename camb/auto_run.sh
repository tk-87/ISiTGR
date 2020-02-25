#!/bin/bash

today=$(date +%Y-%m-%d_%H.%M)
mkdir project/${today}

for i in {0..3}
do
    sed -i -e "6s/.*/Parameterization_BIN = $i/" params_ISiTGR_BIN.ini
    ./camb params.ini
    wait

    if [ $i == 0 ]
    then
        param=default-GR
    elif [ $i == 1 ]
    then
        param=mu-eta
    elif [ $i == 2 ]
    then
        param=mu-sigma
    elif [ $i == 3 ]
    then
        param=Q-D
    fi

    mv test_lensedCls.dat project/${today}/${param}_test_lensedCls.dat
    mv test_lenspotentialCls.dat project/${today}/${param}_test_lenspotentialCls.dat
    mv test_matterpower.dat project/${today}/${param}_test_matterpower.dat
    mv test_params.ini project/${today}/${param}_test_params.ini
    mv test_transfer_out.dat project/${today}/${param}_test_transfer_out.dat
    rm test_scalCls.dat
    rm test_scalCovCls.dat 

done

./project/matter_power_plot.py $today
./project/lens_pot_plot.py $today
