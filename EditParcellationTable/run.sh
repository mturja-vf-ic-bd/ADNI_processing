#!/bin/bash

subjectDir=$1
debug=$2

for file in `ls $subjectDir`; do
	source=$subjectDir/$file/combined.InnerSurface_relabeled.vtk
	if [ -f $source ]
	then
		echo './EditParcellationTable '$source' '$subjectDir/$file' '$debug
		./EditParcellationTable $source $subjectDir/$file $debug
		python rewriteTable.py $subjectDir/$file $subjectDir/parcellationTable.json
	else
		echo 'Error: vtk file missing'
	fi
done
