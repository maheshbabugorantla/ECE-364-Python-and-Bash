#! /bin/bash

if [[ $# < 1 ]]
then
    echo "Usage: $0 <filename>"
    exit 1
fi

for val in $@
do
	if [[ -e $val ]]
	then
		echo "$val exists"
	else
		echo "$val does not exist"
	fi

	if [[ -d $val ]]
	then
		echo "$val is a directory"
	else
		echo "$val is not a directory"
	fi

	if [[ -f $val ]]
	then
		echo "$val is an ordinary file"
	else
		echo "$val is not an ordinary file"
	fi

	if [[ -r $val ]]
	then
		echo "$val is readable"
	else
		echo "$val is not readable"
	fi

	if [[ -w $val ]]
	then
		echo "$val is writable"
	else
		echo "$val is not writable"
	fi
	
	if [[ -x $val ]]
	then
		echo "$val is executable"
	else
		echo "$val is not executable"
	fi
done

exit 0
