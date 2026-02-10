
txt_data = "I got nothing to say!"

file_path = "/home/roger/Desktop/Python Practice/output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print("File has been created")

#to append use "a" instead of "w"                           || this all are modes
#"w" overwrites if a file already exists                    || to write in a file  
#to check if a file already use "x" instead of "w"          || 