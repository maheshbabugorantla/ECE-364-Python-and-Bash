#! /bin/bash

# 2
if [[ $# < 1 ]]
then 
	echo "Usage: ./sort.bash <filename>"
	exit 1
fi

# 3
if [[ ! -e $1 ]]
then
	echo "Error: $1 does not exist"
	exit 2
fi

# 4
echo "The 5 fastest CPUs:"
sort -n -k5 -t ',' simulations.txt | head -n5

echo " "

# 5
echo "The 3 most efficient CPUs:"
sort -n -k4 -t ',' simulations.txt | head -n3

sort -n -k5 -t ',' simulations.txt | tee temp_inc_exec.txt > /dev/null

echo " "

# 6
echo "The CPUs with cache size 4: "

while read line
do
	val=$(echo $line | cut -d ',' -f2 )
	if [[ $val -eq 4 ]]
	then
		echo "$line"
	fi

done < "temp_inc_exec.txt"

rm -f temp_inc_exec.txt > /dev/null

echo " "

# 7

read -p "Enter a value for n: " no_lines
echo "The $no_lines slowest CPUs: "

sort -n -k5 -t ',' -r simulations.txt | head -n$no_lines

echo " "

# 8

sort -n -k4 -t ',' simulations.txt |  tee temp_inc_CPI.txt > /dev/null

touch sorted_CPI.txt

while read line_AMD
do
	val=$(echo $line_AMD | cut -d ',' -f1 )
	
	if [[ $val="AMD Opteron" ]]
	then
		echo "$line_AMD" >> sorted_CPI.txt
	fi


done < "temp_inc_CPI.txt"

while read line_Intel
do
	val=$(echo $line_Intel | cut -d ',' -f1 )

	if [[ $val="Intel Core i7" ]]
	then
		echo "$line_Intel" >> sorted_CPI.txt
	fi

done < "temp_inc_CPI.txt"

rm -f temp_inc_CPI.txt > /dev/null

exit 0
