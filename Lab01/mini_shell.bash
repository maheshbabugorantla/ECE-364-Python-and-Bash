#! /bin/bash

while (true)
do
read -p "Enter a command: " command_val

if [[ $command_val = "hello" ]]
then
	echo "Hello $USER"	

elif [[ $command_val = "compile" ]]
then
	files=$( ls *.c )

	for val in $files
	do
		filename=$( echo $val | cut -d'.' -f1 )
		gcc -Wall -Werror $val -o "$filename.o"

		if (( $? == 0))
		then	
			echo "Compilation succeeded for: $val"
		else
			echo "Compilation failed for: $val"
		fi
	done

elif [[ $command_val == "run" ]]
then
	read -p "Enter filename: " filename_exec
	read -p "Enter arguments: " arguments
	
	

	if [[ ! -e $filename_exec ]] || [[ ! -x $filename_exec ]] 
	then
		echo "Invalid filename"
	else
		./$filename_exec $arguments
	fi 
	
elif [[ $command_val == "quit" ]]
then
	echo "Goodbye"
	exit 0

else
	echo "Error: unrecognized input"	
fi
	echo " "
done
