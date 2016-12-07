#! /bin/bash

# $Author$
# $Date$

function func_a 
{
    # Fill out your answer here.
    return
}

function func_b
{
    # Fill out your answer here
 
	diff "invalid1.sud" "invalid2.sud" > /dev/null
		
	if (( $? == 0 ))
	then
		echo "Files are similar."
	else
		echo "Files are different."
	fi
	
    return
}

function func_c
{
    # Fill out your answer here
	file_val="windows8.c"
	#echo $file_val
	filename=$(echo $file_val | cut -d '.' -f1)    
	
	gcc -Wall -Werror "windows8.c" -o "$filename.out" | tee compile.out
	
	if [[ -e $filename ]]
	then
		./$filename >> compile.out
	fi

	return
}

function func_d 
{
    # Fill out your answer here
	#Arr=("ActivityList.txt" "People.txt" "c.txt" "d.txt" "e.txt")
	Arr=("a.txt" "b.txt" "c.txt" "d.txt" "e.txt")
	let val=$RANDOM%5
	echo $val
	head -n7 ${Arr[$val]} | tail -n3
    return 
}

function func_e
{
    # Fill out your answer here
    val="abracadabra"
	val_array=($val)
	
	for i in ${val_array[*]}
	do
		echo -n " $i"
	done

    return
}

#
# To test your function, you can call it below like this:
#
#func_a
func_b
func_c
#func_d
func_e
	
#

exit 0
