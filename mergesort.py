# Library for Tracking Time Taken for Algorithm Runtime
# Used time.perf_counter() instead of time.time() - More accurate for runtime tracking
import time

# Library for Max Integer in Merge Function
import sys

# Reads FileName and Returns 4 Columned Data Structure where Column 4 is the Sum of Columns 1, 2, and 3
def read_file(FileName):
    # Define and Instantiate Array
    Array=[]

    # Try - Except Block for Cases when Wrong File Name is Given
    try:
        with open(FileName , "r") as File:
            # Loop Through Each Line in File
            for Line in File:
                # Strip Values from Line and Remove Spaces then Store in Values
                Values = [int(Value) for Value in Line.strip().split()]                
                # Store the Values in Array along with Summation of the 3 Columns in Column 4
                Array.append([Values[0] , Values[1] , Values[2] , Values[0] + Values[1] + Values[2]])
    except:
        print(f"File not found")
    
    # Return Newly Formed 4 Tuple Array
    return Array

# Function Merge(Array, P, Q, R)
# Inputs: 1) Array - Some Random Array of Size R
#         2) P - Starting Array Column Value (0 for Python)
#         3) Q - Midpoint of Current Array Size
#         4) R - Size of Current Array
# Returns: Merged Array of Current Array Section
def Merge(Array, P, Q, R):
    N1 = Q - P + 1
    N2 = R - Q

    Left = [0] * (N1 + 1)
    Right = [0] * (N2 + 1)

    # Store Variables from Array into Left and Right Arrays Based on P, Q, and R Values
    for i in range(0, N1):
        Left[i] = Array[P + i] # [i + P - 1] Not Needed Due to Python Lists Starting at 0
    for j in range(0, N2):
        Right[j] = Array[Q + j + 1]

    # Store Max Value in Last Column of Left and Right Arrays
    # 4 Max Sized Ints are Used to Avoid Subscriptable TypeError, Keeps Array as a List
    Left[N1] = [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]
    Right[N2] = [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]

    # Set i and j Value as 0
    # Set k Starting Value as P
    i, j = 0, 0
    k = P

    # Loop Until i > N1 or j > N2
    while i < N1 and j < N2:
        # Comparison for 4th Column Only
        if Left[i][3] < Right[j][3]:
            Array[k] = Left[i]
            i = i + 1
        else:
            Array[k] = Right[j]
            j = j + 1
        k = k + 1

    # Extra Loop if i < N1 after Main Loop
    # Will always be larger - Do Not Need to Compare 4th Column Here
    while i < N1:
        Array[k] = Left[i]
        i = i + 1
        k = k + 1

    # Extra Loop if j < N2 after Main Loop 
    # Will always be larger - Do Not Need to Compare 4th Column Here
    while j < N2:
        Array[k] = Right[j]
        j = j + 1
        k = k + 1


# Function MergeSort(Array, P, R) - Recursive
# Inputs: 1) Array - An Array of Size R
#         2) P - Starting Array Column Value (0 for Python)
#         3) R - Size of Current Array
# Returns: Sorted Array of Current Array Size
def MergeSort(Array, P, R):
    if P < R:
        # Calculate Midpoint of Array and Store Variable in Q
        Q = (P + R) // 2

        # Recursion to Sort then Merge Array
        MergeSort(Array, P, Q)
        MergeSort(Array, Q + 1, R)
        Merge(Array, P, Q, R)


# Function MergeSortWrite(Array, FileSize)
# Inputs: 1) Array - An Array of Varying Size (20, 100, 2000, 6000)
#         2) FileSize - Current Size of File We Wish to Sort
# No Returns: Writes Sorted Array to Designated Output File
def MergeSortWrite(Array , FileSize):
    # Start Time of Sorting to Track Runtime
    StartTime = time.perf_counter()
    print(StartTime)

    # Main Call to Recursive MergeSort Algorithm
    MergeSort(Array, 0, len(Array) - 1)
    
    # End Time of Sorting to Track Runtime
    EndTime = time.perf_counter()
    print(EndTime)

    # Open New File and Write Sorted Array to File
    with open('arrMR_O_'+str(FileSize)+'.txt' , 'w') as File:
        for Row in Array:
            File.write(" ".join(map(str, Row)))
            File.write('\n')
        
        # Appends Runtime of Algorithm to End of .txt File
        File.write("Total runtime: " + str(EndTime-StartTime) + " seconds")


# Define and Instantiate File Sizes We Will Sort Through
Size = [20, 100, 2000, 6000]

# Loop Through the 4 Files We Wish to Sort
for FileSize in Size:
    Array = read_file('arr'+str(FileSize)+'.txt')
    MergeSortWrite(Array , FileSize)
    print(f"Done with file of size {FileSize}")