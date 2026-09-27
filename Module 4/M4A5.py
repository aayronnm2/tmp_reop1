# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }

for person, food in food_dict.items():
    if food == '':
        newFood = input(f"What is {person}'s favorite food? ")
        food_dict[person] = newFood

print(f"Here are the favorite foods:")

for person, food in food_dict.items():
    print(f"{person}'s favorite food is {food}")