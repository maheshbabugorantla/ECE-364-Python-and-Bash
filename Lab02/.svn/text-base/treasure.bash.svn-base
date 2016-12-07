#! /bin/bash

if [[ $# < 1 ]]
then
	echo "Usage: ./treasure.bash <filename>"
	exit 1
fi

row_count=0
while read line
do
	let row_count=$row_count+1
done < $1

counter=0
while read line_val
do	
	for val in $line_val
	do
		array[counter]=$val
		let counter=$counter+1
	done	

done < $1


row_index=0

echo "(0,0)"
val=${array[0]}
let tens=$val/10
let ones=$val%10

echo "($tens,$ones)"

tens=0
ones=0

let rows=$row_count-1

let max_index=$row_count*$rows
let max_index=$max_index+$rows

while [[ $row_index < $max_index ]]
do

	let index=$tens*$row_count
	let index=$index+$ones	
	val=${array[$index]}

	let tens=$val/10
	let ones=$val%10
	let new_index=$tens*$row_count
	let new_index=$new_index+$ones
	new_value=${array[$new_index]}
	let tens=$new_value/10
	let ones=$new_value%10

	echo "($tens,$ones)" 		

	row_index=$new_index
	let row_index=$row_index+1

done < $1

exit 0
