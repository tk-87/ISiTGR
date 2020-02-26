#!/bin/bash

today=$(date +%Y-%m-%d_%H.%M)
cd /home/tony/ISiTGR/camb/
mkdir -p project/${today}/lensedCls
mkdir -p project/${today}/lenspotentialCls
mkdir -p project/${today}/matterpower
mkdir -p project/${today}/params
mkdir -p project/${today}/transfer_out

# makes sure that Parameterization = 2 (mu-sigma)
sed -i -e "6s/.*/Parameterization_BIN = 2/" params_ISiTGR_BIN.ini

for i in {1..3}
do
    for j in {1..9}
    do
        n=0.$j

        if [ $i -eq 1 ]
        then

            name="mu-${n}_sig-${n}"

            sed -i -e "27s/.*/mu1 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "28s/.*/mu2 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "29s/.*/mu3 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "30s/.*/mu4 = ${n}/" params_ISiTGR_BIN.ini

            sed -i -e "39s/.*/Sigma1 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "40s/.*/Sigma2 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "41s/.*/Sigma3 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "42s/.*/Sigma4 = ${n}/" params_ISiTGR_BIN.ini

        elif [ $i -eq 2 ]
        then

            if [ $j -eq 1 ]
            then
                continue
            fi

            name="mu-${n}_sig-0.1"

            sed -i -e "27s/.*/mu1 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "28s/.*/mu2 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "29s/.*/mu3 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "30s/.*/mu4 = ${n}/" params_ISiTGR_BIN.ini

            sed -i -e "39s/.*/Sigma1 = 0.1/" params_ISiTGR_BIN.ini
            sed -i -e "40s/.*/Sigma2 = 0.1/" params_ISiTGR_BIN.ini
            sed -i -e "41s/.*/Sigma3 = 0.1/" params_ISiTGR_BIN.ini
            sed -i -e "42s/.*/Sigma4 = 0.1/" params_ISiTGR_BIN.ini

        elif [ $i -eq 3 ]
        then

            if [ $j -eq 1 ]
            then
                continue
            fi

            name="mu-0.1_sig-${n}"

            sed -i -e "27s/.*/mu1 = 0.1/" params_ISiTGR_BIN.ini
            sed -i -e "28s/.*/mu2 = 0.1/" params_ISiTGR_BIN.ini
            sed -i -e "29s/.*/mu3 = 0.1/" params_ISiTGR_BIN.ini
            sed -i -e "30s/.*/mu4 = 0.1/" params_ISiTGR_BIN.ini

            sed -i -e "39s/.*/Sigma1 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "40s/.*/Sigma2 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "41s/.*/Sigma3 = ${n}/" params_ISiTGR_BIN.ini
            sed -i -e "42s/.*/Sigma4 = ${n}/" params_ISiTGR_BIN.ini

        fi

        ./camb params.ini
        wait

        mv test_lensedCls.dat project/${today}/lensedCls/${name}.dat
        mv test_lenspotentialCls.dat project/${today}/lenspotentialCls/${name}.dat
        mv test_matterpower.dat project/${today}/matterpower/${name}.dat
        mv test_params.ini project/${today}/params/${name}.ini
        mv test_transfer_out.dat project/${today}/transfer_out/${name}.dat
        rm test_scalCls.dat
        rm test_scalCovCls.dat

    done

    ./project/MP_plot_variable.py $today $i $j
    ./project/LP_plot_variable.py $today $i $j

done
