# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 4 Assignment 2

food_dict = {}

for num in range(1,4):
    food = input("What is good to eat? ")
    country = input("What country is that from? ")
    food_dict[food] = {country}

dish = input("What dish do you like? ")

for dishes, country in food_dict.items():
    if dish in dishes and dishes == dish:
        print(f'{dishes} is from {list(country)[0]}')