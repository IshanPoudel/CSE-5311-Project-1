#Create a function to generate filkes
import random
import time

def generate_file():
    file_size=[20,100,2000,6000]

    for num in file_size:
        file_name = "arr"+str(num)+".txt"
        #Open the file
        with open(file_name , "w") as file:
            #Run a for loop
            for i in range(num):
                random_numbers = [random.randint(1, 100) for _ in range(3)]
                file.write(" ".join(map(str, random_numbers)))
                file.write("\n")
        
        print(f"Done generating size {num}")



def read_file(file_name ):

    #Reads a file _name and returns a 4 columned data strucutre where the fourth column is the sum
    arr=[]

    try:
        with open(file_name , "r") as file:
            #Open each line
            for line in file:
                #Strip values
                values = [int(value) for value in line.strip().split()]                
                #Store the value in an array
                arr.append([values[0] , values[1] , values[2] , values[0]+values[1]+values[2]])



    except:
        print(f"File not found")
    
    return arr



def insertion_sort(arr , file_size):

    # The function takes the arr
    # Sorts it using the algorithm
    # Tracks the runtime of the sorting algorithm 
    # Writes to an output file

    #Get the size of the arr 

    start_time = time.time()

    size = len(arr)

    for i in range(1 , size):
        j=i-1
        key_arr = arr[i]
        key = arr[i][3]

        while j>=0 and key<arr[j][3]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key_arr
    
    end_time = time.time()

    #Need to print a file output
    with open('arrIS_O_'+str(file_size)+'.txt' , 'w') as file:
        for row in arr:
            file.write(" ".join(map(str, row)))
            file.write('\n')
        
        file.write("Total runtime: " + str(end_time-start_time) + " seconds")



    
    
#To generate new files
generate_file()


size = [20 , 100 , 2000 , 6000]

for file_size in size:
    arr = read_file('arr'+str(file_size)+'.txt')
    insertion_sort(arr , file_size)
    print(f"Done with file of size {file_size}")





