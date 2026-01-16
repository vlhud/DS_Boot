#!/bin/sh

echo "\"name\",\"count\"" > hh_uniq_positions.csv
awk -F',' 'NR>1 {print $3}' ../ex03/hh_positions.csv | sort | uniq -c | sort -nr | awk '{print($2","$1)}' >> hh_uniq_positions.csv