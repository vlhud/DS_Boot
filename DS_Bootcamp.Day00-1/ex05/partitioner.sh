#!/bin/sh

awk -F"," 'NR > 1 { split($2, a, "T"); 
    date = a[1]; 
    print date, $0 }' ../ex03/hh_positions.csv | while read date record
do
    if [ ! -f "$date.csv" ]; then
        head -n1 ../ex03/hh_positions.csv > $date.csv
    fi
    echo $record >> $date.csv
done