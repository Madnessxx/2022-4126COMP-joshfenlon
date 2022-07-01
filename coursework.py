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
print("")
choice = (input("Make your choice: "))

#search for keyword

if (choice == "1"):
    print()

#Search for data in a specific region

if (choice == "2"):
    data2 = input("Enter the data that you want to search by")
    region2 = input("Enter the region you want to filter by")
    print(df[data2].where(df[region2]))

#show entire dataset

if (choice == "3"):
    print(df) #prints the entire dataset

