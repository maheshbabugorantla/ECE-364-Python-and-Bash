#! /bin/bash

if [[ $# -ne 1 ]]
then
    echo "Usage: line_num.bash <filename>"
    exit 1
fi

if [[ ! -r $1 ]] 
then
    echo "Cannot read $1"
    exit 2
elif [[ ! -e $1 ]]
then
    echo "$1 file or directory does not exist"
    exit 3
fi

Counter=1

while IFS= read -r line; do
   echo "$Counter:$line"
   (( Counter+=1 ))
done < "$1"

exit 0
