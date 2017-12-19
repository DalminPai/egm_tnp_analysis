#!/bin/bash


fitter=$1         ### ex) tnpEGM_fitter.py
#script=$2         ### ex) settings.py

script1="etc/config/settings_ele_runGH12to29.py"
script2="etc/config/settings_ele_runGH30to39.py"

flags=(
#    "passingVeto80X"
    "passingMedium80X"
#    "passingLoose80X"
#    "passingTight80X"
#    "passingTight"
    "passingMVA80Xwp80"
    "passingMVA80Xwp90"
#    "passingMVAwp80"
#    "passingMVAwp90"
#    "passingRECO"
)

for flag in ${flags[@]}; do
    echo $fitter
#    echo $script

    echo $script1
    echo $script2

    echo $flag
    #python tnpEGM_fitter.py  $script --flag $flag --createBins
    #python tnpEGM_fitter.py  $script --flag $flag --createHists
    #python tnpEGM_fitter.py  $script --flag $flag --doFit
    #python tnpEGM_fitter.py  $script --flag $flag --doFit --mcSig --altSig
    #python tnpEGM_fitter.py  $script --flag $flag --doFit --altSig
    #python tnpEGM_fitter.py  $script --flag $flag --doFit --altBkg
    #python tnpEGM_fitter.py  $script --flag $flag --sumUp
#    python $fitter  $script --flag $flag --createBins
#    python $fitter  $script --flag $flag --createHists
#    python $fitter  $script --flag $flag --doFit

#    python $fitter  $script --flag $flag --doFit --mcSig --altSig
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 12
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 17
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 20
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 21
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 22
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 24
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 26
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 27
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 28
    python $fitter  $script1 --flag $flag --doFit --mcSig --altSig --iBin 29
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 30
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 31
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 32
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 33
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 34
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 35
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 36
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 37
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 38
    python $fitter  $script2 --flag $flag --doFit --mcSig --altSig --iBin 39

#    python $fitter  $script --flag $flag --doFit --altSig
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 12
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 17
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 20
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 21
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 22
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 24
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 26
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 27
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 28
    python $fitter  $script1 --flag $flag --doFit --altSig --iBin 29
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 30
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 31
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 32
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 33
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 34
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 35
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 36
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 37
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 38
    python $fitter  $script2 --flag $flag --doFit --altSig --iBin 39

    python $fitter  $script2 --flag $flag --doFit --altBkg
    python $fitter  $script2 --flag $flag --sumUp
done


