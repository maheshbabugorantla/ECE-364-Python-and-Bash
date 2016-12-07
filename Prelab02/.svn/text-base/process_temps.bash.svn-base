#! /bin/bash

if [[ $# != 1 ]]
then
	echo "Usage: process_temps.bash <input file>"
	exit 1
fi

if [[ ! -r $1 ]]
then
	echo "Error: $1 is not a readable file."
	exit 2
fi

tail -n+2 $1 | tee "$1.out" > /dev/null #&& readarray array_val < "$1.out"


while read line; do

	temps=($(echo $line | cut -d ' ' -f1-))
	
	temp_sum=0
	temp_count=0

	for index_val in ${!temps[*]}
	do
		if [[ index_val -gt 0 ]]
		then
			let temp_sum+=${temps[index_val]}
			let temp_count+=1
		fi
	
	done
	
	let temp_average=$temp_sum/$temp_count
#	echo $temp_average
	echo "Average temperature for time ${temps[0]} was $temp_average C."	
done < "$1.out"

rm "$1.out"

exit 0
