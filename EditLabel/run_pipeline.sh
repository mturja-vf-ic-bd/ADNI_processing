#!/bin/bash

debug=$1
root="/home/turja/Desktop/ADNI_processing"
subDir="${root}/sub"
cmake .
make -j4
${root}/EditLabel/./relabelVtk.sh $subDir $debug
${root}/EditParcellationTable/./run.sh $subDir $debug