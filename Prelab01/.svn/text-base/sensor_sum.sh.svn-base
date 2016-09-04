#! /bin/bash

if [[ $# < 1 ]]
then
	echo "usage: sensor_sum.sh log"
	exit 1
fi

if [[ ! -r $1 ]]
then
	echo "error: $1 is not a readable file!"
	exit 2
fi

while read temp1 temp2 temp3 temp4; do
	let Sum=$temp2+$temp3+$temp4
	var=$(echo $temp1 | cut -d '-' -f1)
	echo "$var $Sum"

#while IFS= read -r line; do
#	echo $line
done < "$1"
