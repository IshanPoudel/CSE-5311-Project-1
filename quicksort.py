# Library for Creating arrXXX.txt Files with Random Number Generation
import random

# Library for Tracking Time Taken for Algorithm Runtime
import time


# Reads FileName and Returns 4 Columned Data Structure where Column 4 is the Sum of Columns 1, 2, and 3
def read_file(file_name ):
    # Define and Instantiate Array
    arr=[]

    # Try - Except Block for Cases when Wrong File Name is Given
    try:
        with open(file_name , "r") as file:
            # Loop Through Each Line in File
            for line in file:
                # Strip Values from Line and Remove Spaces then Store in Values
                values = [int(value) for value in line.strip().split()]                
                # Store the Values in Array along with Summation of the 3 Columns in Column 4
                arr.append([values[0] , values[1] , values[2] , values[0]+values[1]+values[2]])
    except:
        print(f"File not found")
    
    # Return Newly Formed 4 Tuple Array
    return arr


def quicksort(arr):

    if len(arr) <= 1:
        return arr
    
    #Pick the middle as the pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[3] < pivot[3]]
    middle = [x for x in arr if x[3] == pivot[3]]
    right = [x for x in arr if x[3] > pivot[3]]

    return quicksort(left) + middle + quicksort(right)


def quick_sort_write(arr , file_size):

    # The function takes the arr
    # Sorts it using the algorithm
    # Tracks the runtime of the sorting algorithm 
    # Writes to an output file

    #Get the size of the arr 

    start_time = time.perf_counter()

    size = len(arr)

    arr=quicksort(arr)
    
    end_time = time.perf_counter()

    #Need to print a file output
    with open('arrQK_O_'+str(file_size)+'.txt' , 'w') as file:
        for row in arr:
            file.write(" ".join(map(str, row)))
            file.write('\n')
        
        file.write("Total runtime: " + str(end_time-start_time) + " seconds")


# Define and Instantiate File Sizes We Will Sort Through
size = [20 , 100 , 2000 , 6000]

# Loop Through the 4 Files We Wish to Sort
for file_size in size:
    arr = read_file('arr'+str(file_size)+'.txt')
    quick_sort_write(arr , file_size)
    print(f"Done with file of size {file_size}")





