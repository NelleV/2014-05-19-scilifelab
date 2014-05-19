# for an input file, 
# list the country with the highest life expectancy

year=$1
sort -nr -k 5 $year | head -n 1

