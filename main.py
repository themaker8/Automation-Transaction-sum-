import csv

#Some variable needed for our application
file_name = input("ENTER YOUR FILE PATH: ")
column = input("Enter your file column name to sum up: ")


def main():
#opening the file 
    with open(file_name) as file:
        total = sum(int(r[column]) for r in csv.DictReader(file))
        print(f'The total expense is : {total}')


main()
