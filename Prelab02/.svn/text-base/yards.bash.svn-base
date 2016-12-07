#! /bin/bash

if [[ $# < 1 ]]
then
	echo "Usage: yards.bash <filename>"
	exit 1
fi

if [[ ! -e $1 ]] || [[ ! -r $1 ]]
then
	echo "Error: $1 is not readable"
	exit 2
fi
	max_average=0
	while read line; do
		values=($(echo $line | cut -d ' ' -f2-))
		sum_val=0
		count=0
		for val in ${values[*]}
		do
			let sum_val+=$val
			let count+=1
		done		

		average=0		
		((average=$sum_val/$count))	

#		echo "Average is $average"

		if [[ $average -gt $max_average ]]
		then
			let max_average=$average
		fi
		
		sum_powers=0
		diff_val=0
		for val_1 in ${values[*]}
		do
			let diff_val=$val_1-$average
			let sum_powers+=$diff_val*$diff_val	
		done
		variance=0
		((variance=$sum_powers/$count))		
#		echo "Variance is $variance"
		
		school_name=$(echo $line | cut -d ' ' -f1)
		echo "$school_name schools averaged $average yards receiving with a variance of $variance"
	done < "$1"
	
	echo "The largest average yardage was $max_average"

exit 0
