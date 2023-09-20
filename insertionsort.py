#Create a function to generate filkes
import random

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


arr = read_file('arr20.txt')
