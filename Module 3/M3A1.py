# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 3 Assignment 1

start_int = input("What is the first number? ")
end_int = input("What is the second number? ")

num_list = range(int(start_int),int(end_int)+1)
sum_int = 0
for n in num_list:
    sum_int += n

print(f"The total value of numbers from {start_int} to {end_int} is {sum_int}")