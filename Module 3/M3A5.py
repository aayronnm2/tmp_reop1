# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 3 Assignment 5

start_int = input("What is the first number? ")
end_int = input("What is the second number? ")

num_list = range(int(start_int),int(end_int)+1)
sum_int = 0
for n in num_list:
    if n % 5 == 0:
        sum_int += n

print(f"The total value of multiples of 5 from {start_int} to {end_int} is {sum_int}")