#!/bin/sh

head -n1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n+2 ../ex02/hh_sorted.csv | awk -v FPAT='"[^"]*"|[^,]*' '
    BEGIN { OFS = "," }
    {
      name = $3
      gsub(/"/, "", name)
      found_words = "" 
      if (name ~ /Junior/) found_words=found_words"Junior"; 
      if (name ~ /Middle/) found_words=found_words"Middle"; 
      if (name ~ /Senior/) found_words=found_words"Senior";  
      if (found_words == "") found_words = "-"; 
    print $1, $2, "\"" found_words "\"", $4, $5}' >> hh_positions.csv