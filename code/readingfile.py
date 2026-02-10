import csv

file_path = "input.csv"             #write your files relative address 
try:
    with open(file_path, "r") as file:
        reader = csv.reader(file)

        header = next(reader)

        row_format = "| {:<10} | {:<5} | {:<12} |"

        print("_" * 3)
        print(row_format.format(*header))
        print("|" + "-" * 35 + "|")

        for row in reader:
            print(row_format.format(*row))

except FileNotFoundError:                   #You can add more except command
    print("File not found!")   

#This is a csv reading file example
#Use json.dump() and json.load() to write and read files in json
#And reading in txt is easy as fuck 
