#! /bin/bash

Sum=0
 
#for val in $@
#do
#    ((Sum+=val))
#done

while [ -n "$1" ]; do
    ((Sum=Sum+$1))
    shift
done

echo "$Sum"

exit 0
