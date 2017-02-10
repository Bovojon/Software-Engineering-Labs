#!/bin/bash

FILES=path/to/test_files/*

echo "Do you want to run quicksort on all files in $FILES (Type y/n)?"
read answer

if [ $answer = y ]; then
    for filename in $FILES
    do
        fileLength=$(wc -l < $filename)
        echo "Your file, $filename, has $fileLength lines."
        ./quicksort $filename $fileLength 0
        echo ""
        ./quicksort $filename $fileLength 1
        echo ""
    done
else
    echo "Enter the filename you would like to run quicksort on:"
    read filename

    fileLength=$(wc -l < $filename)
    echo "Your file, $filename, has $fileLength lines."
    ./quicksort $filename $fileLength 0
    echo ""
    ./quicksort $filename $fileLength 1
    echo ""
