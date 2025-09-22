#!/bin/bash

# Launch Scrapy spiders for each urls*.txt file and create corresponding output CSV files
# Collect execution times for each operation

# Akamai
start_time=$(date +%s.%N)
scrapy crawl test -a input_file=urls_akamai.txt -a output_file=output_akamai.csv
end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)
echo "Akamai: ${duration} seconds" >> execution_times.txt

# Cloudflare
start_time=$(date +%s.%N)
scrapy crawl test -a input_file=urls_cloudflare.txt -a output_file=output_cloudflare.csv
end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)
echo "Cloudflare: ${duration} seconds" >> execution_times.txt

# DataDome
start_time=$(date +%s.%N)
scrapy crawl test -a input_file=urls_datadome.txt -a output_file=output_datadome.csv
end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)
echo "DataDome: ${duration} seconds" >> execution_times.txt

# Kasada
start_time=$(date +%s.%N)
scrapy crawl test -a input_file=urls_kasada.txt -a output_file=output_kasada.csv
end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)
echo "Kasada: ${duration} seconds" >> execution_times.txt

# PerimeterX
start_time=$(date +%s.%N)
scrapy crawl test -a input_file=urls_perimeterx.txt -a output_file=output_perimeterx.csv
end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)
echo "PerimeterX: ${duration} seconds" >> execution_times.txt 