import csv
import pandas as pd

df = pd.read_csv("dataset/avocado.csv")


#i want to start getting user inputs
#i need to set up a menu system

print("Hi, what would you like to do?")
print("1. Search for keyword")
print("2. Search for data in a specific region")
print("3. Show Entire dataset")
print("4. Convert csv to txt")
print()
choice = (input("Make your choice: "))

#search for keyword

if (choice == "1"):
    data1 = input("Enter the keyword: ")
    print(df[data1])

#Search for data in a specific region

if (choice == "2"):
    data2 = input("Enter the data that you want to search by: ")
    region2 = input("Enter the region you want to filter by: ")
    # print(df[data2].where(df['region'] = region2)) #couldnt get this to work

#show entire dataset

if (choice == "3"):
    print(df) #prints the entire dataset

#Convert csv to txt

if (choice == "4"):
    print("")

#opening csv file in reading mode and txt file in writing mode
with open('dataset/avocado.csv', 'r') as f_in, open('text/avovado.txt', 'w') as f_out:
    content = f_in.read() # read the csv values and store in variable
    f_out.write(content) # write the content into the txt file