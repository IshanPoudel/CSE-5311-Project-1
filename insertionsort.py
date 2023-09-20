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


generate_file()



