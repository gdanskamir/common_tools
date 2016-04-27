#!/bin/bash


out=$1;


awk -F'\t' -v out=${out} 'BEGIN {
    count = 0;
    srand();
} {
    count = count + 1;
    if (count <= out)  {
        dict[count] = $0;
    } else { 
        rand_num = int(rand() * count) + 1;
        if (rand_num <= out) {
            dict[rand_num] = $0;   
        }
    }
} END {
    for (i in dict) {
        print dict[i];    
    }
}'
