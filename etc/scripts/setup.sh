#!/bin/bash


#fitter=$1         ### ex) tnpEGM_fitter.py
script=$1
#Bin=$1
flags=(
#    "passingVeto80X"
#    "passingMedium80X"
#    "passingLoose80X"
#    "passingTight80X"
#    "passingTight"
#    "passingMVA80Xwp80"
#    "passingMVA80Xwp90"
#    "passingMVAwp80"
#    "passingMVAwp90"
#    "passingRECO"
#    "passingHLT"
#    "passingHNEleID"
    "passingHNEleID_v2"
)

for flag in ${flags[@]}; do
#    echo $fitter
    echo $script
    echo $flag
    python tnpEGM_fitter.py  $script --flag $flag --createBins
    python tnpEGM_fitter.py  $script --flag $flag --createHists
    python tnpEGM_fitter.py  $script --flag $flag --doFit
#    python tnpEGM_fitter.py  $script --flag $flag --doFit --mcSig --altSig
#    python tnpEGM_fitter.py  $script --flag $flag --doFit --mcSig --altSig --iBin $Bin
#    python tnpEGM_fitter.py  $script --flag $flag --doFit --altSig
#    python tnpEGM_fitter.py  $script --flag $flag --doFit --altSig --iBin $Bin
#    python tnpEGM_fitter.py  $script --flag $flag --doFit --altBkg
    echo "Fit is finished"
    python tnpEGM_fitter.py  $script --flag $flag --sumUp
    echo "Job is finished"
done


