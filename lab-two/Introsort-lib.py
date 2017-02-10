import time
import timeit
import sys
from IntroSort import *


def get_input_ints():
    files = ["ints-1.dat", "ints-100k.dat", "ints-10k.dat", "ints-1m.dat", "ints-10m.dat"]
    print("The files available to test are: \n")
    print(files)
    print("\n")
    fileName = input("Input file name: ")
    f = open(fileName, 'r')
    arrayNum = []
    for line in f:
        line.strip()
        arrayNum.append(int(line))
    f.close()
    return arrayNum

    
def time_introsort():
    arrayNum = get_input_ints()
    timeIntrosort, newArray = find_average(arrayNum)
    return timeIntrosort, newArray, arrayNum

        
def run_individually():
    timeIntrosort, newArray, arrayNum = time_introsort()
    optionInput = input("Would you like to display input array? (Type y/n) ")
    if optionInput == "y":
        print("The input array was: \n")
        print(arrayNum)
    else:
        pass 
    print("\n")
    print("The time taken to quicksort the array in seconds is: \n")
    print(timeIntrosort)
    print("\n")
    
    test_sorted(newArray)
    optionOutput = input("Would you like to display sorted array? (Type y/n) ")
    if optionOutput == "y":
        print("The new sorted array is: \n")
        print(newArray)
        print("\n")
        
    # Save the sorted array to a file
    optionToWrite = input("Save sorted array in a file? (Type y/n) ")
    if optionToWrite == "y":
        fileSaveAs = input("Save file as (without extension): ")
        fileToWrite = open(fileSaveAs+".dat", 'w')
        for item in newArray:
            fileToWrite.write("%d\n" % item)
    elif optionToWrite == "n":
        print("Thank you!")

            
def run_bulk():
    files = ["ints-1.dat", "ints-100k.dat", "ints-10k.dat", "ints-1m.dat", "ints-10m.dat"]
    
    # Create new file called times.dat and close it
    ft = open("times.dat", "w")
    ft.write("Jon Lab2 | Results file | Software Engineering\n")
    ft.close()
    
    for afile in files:

        # Open file and store its content in an array 
        arrayNum = open_file(afile)
        
        # Find the average time for sorting file
        averageTime, newArray = find_average(arrayNum)
        
        # Print and save processed data
        processed_data(afile, averageTime, newArray)
        
    print("The above information is stored in the file times.dat") 
        
        
def processed_data(afile, averageTime, newArray):
    
    #Open file times.dat to append data
    ft = open("times.dat", "a")
    
    if afile == "ints-1.dat":
        print("Average Time for ints-1.dat is ")
        print(averageTime)
        print("\n")
        ratePerInt = (29/averageTime)
        ft.write("The average time (in seconds) to quicksort 29 integers is %s.\n" % averageTime)
        ft.write("If there are 29 integers, it can sort %s integers/second.\n" % ratePerInt)
        ft.write("The sorted array is stored in the file called outputOne.dat \n")
        ft.write("\n")
        ff = open("outputOne.dat", "w")
        for item in newArray:
            ff.write("%s\n" % item)
            
    if afile == "ints-10k.dat":   
        print("Average Time for ints-10k is ")
        print(averageTime)
        print("\n")
        ratePerInt = (10000/averageTime)
        ft.write("The average time (in seconds) to quicksort 10000 integers is %s.\n" % averageTime)
        ft.write("If there are 10000 integers, it can sort %s integers/second.\n" % ratePerInt)
        ft.write("The sorted array is stored in the file called outputThousand.dat \n")
        ft.write("\n")
        ff = open("outputThousand.dat", "w")
        for item in newArray:
            ff.write("%s\n" % item)
    
    if afile == "ints-100k.dat":
        print("Average Time for ints-100k is ")
        print(averageTime)
        print("\n")
        ratePerInt = (100000/averageTime)
        ft.write("The average time (in seconds) to quicksort 100000 integers is %s.\n" % averageTime)
        ft.write("If there are 100000 integers, it can sort %s integers/second.\n" % ratePerInt)
        ft.write("The sorted array is stored in the file called outputHundred.dat \n")
        ft.write("\n")
        ff = open("outputHundred.dat", "w")
        for item in newArray:
            ff.write("%s\n" % item)
                
    if afile == "ints-1m.dat":   
        print("Average Time for ints-1m is ")
        print(averageTime)
        print("\n")
        ratePerInt = (1000000/averageTime)
        ft.write("The average time (in seconds) to quicksort 1,000,000 integers is %s.\n" % averageTime)
        ft.write("If there are 1,000,000 integers, it can sort %s integers/second.\n" % ratePerInt)
        ft.write("The sorted array is stored in the file called outputMillion.dat \n")
        ft.write("\n")
        ff = open("outputMillion.dat", "w")
        for item in newArray:
            ff.write("%s\n" % item)
            
    if afile == "ints-10m.dat":   
        print("Average Time for ints-10m is ")
        print(averageTime)
        print("\n")
        ratePerInt = (10000000/averageTime)
        ft.write("The average time (in seconds) to quicksort 10,000,000 integers is %s.\n" % averageTime)
        ft.write("If there are 10,000,000 integers, it can sort %s integers/second.\n" % ratePerInt)
        ft.write("The sorted array is stored in the file called outputTenMillion.dat \n")
        ft.write("\n")
        ff = open("outputTenMillion.dat", "w")
        for item in newArray:
            ff.write("%s\n" % item)
                   
    ft.close()
      
    
def open_file(afile):
    f = open(afile, 'r')
    arrayNum = []
    for line in f:
        line.strip()
        arrayNum.append(int(line))
    return arrayNum
    f.close()
    
def find_average(arrayNum):
    arrayTimes = []
    for i in range(3):
        start = time.time()
        newArray = introsort(arrayNum)
        end = time.time()
        timeIntrosort = end - start
        arrayTimes.append(timeIntrosort)           
    averageTime = sum(arrayTimes)/len(arrayTimes)
    return averageTime, newArray
    
    
def test_sorted(array):
    pass
    
    
    
def interface_design():
    optionBulk = input("Run files individually or in bulk? Type(i/b): ")
    if optionBulk == "i":
        run_individually()
    elif optionBulk == "b":
        run_bulk()
        
        

if __name__ == '__main__':
    interface_design()
    