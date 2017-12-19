#!/bin/bash


fitType=$1
bin=$2

if [ $fitType = "mc" ]
then
    dir="results/Moriond17/tnpEleID/HN_v2/passingHNEleID/plots/DY_madgraph_Winter17/altSigFit"
elif [ $fitType = "data" ]
then
    #dir="results/Moriond17/tnpEleID/HN_v2/passingHNEleID/plots/data_Run2016H/altSigFit"
    dir="results/Moriond17/tnpEleID/HN_dxy/passingHNEleID_dxy/plots/data_Run2016H/nominalFit"
fi

echo "$dir : bin$bin"
display $dir/bin$bin*


