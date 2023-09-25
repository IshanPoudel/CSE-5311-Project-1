#Create a function to generate filkes
import random

# Library for Max Integer in Merge Function
import time

# Function generate_file()
# Inputs: None
# Purpose: Creates Initial arrXXXX.txt Files with 3 Columns
#          of Randomly Generated Variables
# Returns: None
def generate_file():
    file_size=[20,100,2000,6000]

    # Loop Through the 4 File Sizes
    for num in file_size:
        # Define the File Name Based on num
        file_name = "arr"+str(num)+".txt"

        # Open the File - Creates File if it Doesn't Exist
        with open(file_name , "w") as file:
            # Loop to Generate i Random Variables Based on num Size
            for i in range(num):
                random_numbers = [random.randint(1, 100) for _ in range(3)]
                file.write(" ".join(map(str, random_numbers)))
                file.write("\n")
        
        print(f"Done generating size {num}")

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



def insertion_sort(arr , file_size):

    # The function takes the arr
    # Sorts it using the algorithm
    # Tracks the runtime of the sorting algorithm 
    # Writes to an output file

    #Get the size of the arr 

    start_time = time.perf_counter()

    size = len(arr)

    for i in range(1 , size):
        j=i-1
        key_arr = arr[i]
        key = arr[i][3]

        while j>=0 and key<arr[j][3]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key_arr
    
    end_time = time.perf_counter()

    #Need to print a file output
    with open('arrIS_O_'+str(file_size)+'.txt' , 'w') as file:
        for row in arr:
            file.write(" ".join(map(str, row)))
            file.write('\n')
        
        file.write("Total runtime: " + str(end_time-start_time) + " seconds")


# Function Call To Generate New arrXXXX.txt Files
generate_file()

# Define and Instantiate File Sizes We Will Sort Through
size = [20 , 100 , 2000 , 6000]

# Loop Through the 4 Files We Wish to Sort
for file_size in size:
    arr = read_file('arr'+str(file_size)+'.txt')
    insertion_sort(arr , file_size)
    print(f"Done with file of size {file_size}")





