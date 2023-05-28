#!/bin/bash

user=$(whoami)
date=$(date)

cat dataset_func.txt | cut -d ":" -f 2- | sort >> dataset_sorted.txt
echo "$user - $date" >> dataset_sorted.txt
