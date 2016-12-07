#! /bin/bash

if [[ $# != 2 ]]
then
	echo "Usage: ./run_bash <simulator_source_code> <output_filename>"
	exit 1
fi

binary_comp=$(echo $1 | cut -d'.' -f1)

output_file=$2

if [[ -e $output_file ]]
then
	read -p "$output_file exists. Would you like to delete it? " del_ind

	if [[ $del_ind = "n" ]]
	then
		read -p "Enter a new filename: " output_file
		touch $output_file

#		if [[ -e $output_file ]]
#		then	
#			echo "Output file is $output_file"
#		fi		

		rm $2 > /dev/null
	
	else
		rm $2 > /dev/null
		touch $2
		output_file=$2
	fi
else
	touch $output_file
fi

cache_sizes=(1 2 4 8 16 32)
issue_widths=(1 2 4 8 16)

#if [[ -e $output_file ]]
#then
#	echo "The $output_file is created"
#fi

gcc $1 -o $binary_comp

if [[ $? == 0 ]]
then
	for val_cache in ${cache_sizes[*]}
	do
		for val_issue in ${issue_widths[*]}
		do
			$binary_comp $val_cache $val_issue 'a' |  cut -d ':' -f2-2,4-4,6-6,8-8,10-10 >> $output_file
			$binary_comp $val_cache $val_issue 'i' |  cut -d ':' -f2-2,4-4,6-6,8-8,10-10 >> $output_file
		done
	done
else
	echo "error: quick_sim could not be compiled"
	rm $output_file > /dev/null
fi

exit 0
