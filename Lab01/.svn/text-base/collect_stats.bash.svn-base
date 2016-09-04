#! /bin/bash

if [[ $# < 2 ]]
then
	echo "Usage: ./collect_stats.bash <file> <sport>"
	exit 1
fi

if [[ ! -e $1 ]]
then
	echo "Error: someFile does not exist"
	exit 2
fi

no_people=0
no_medals=0
max_medals=0
max_person=""

while read line; do
	
	name=$( echo $line | cut -d, -f1 )
	sport=$( echo $line | cut -d, -f2 )
	medals=$( echo $line | cut -d, -f3 )
	
	if [[ $sport = $2 ]]
	then	
		let no_people+=1
		let no_medals+=$medals
		
		if [[ $medals -gt $max_medals ]]
		then
			max_medals=$medals
			max_person=$name
		fi
	fi

done < "$1"

echo "Total athletes: $no_people"
echo "Total medals won: $no_medals"
echo "$max_person won the most medals: $max_medals"

exit 0
