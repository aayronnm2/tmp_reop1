# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 2 Assignment 3

uber_list = range(100,201,2)

startslice = int(input("What is the start of your slice? "))
endslice = int(input("What is the end of your slice? "))
data_list = uber_list[startslice:endslice]

total_int = 0
for n in data_list:
    total_int += n

print(f"Your slice contains {len(data_list)} values and has an average value of {total_int / len(data_list)}")