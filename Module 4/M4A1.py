# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 4 Assignment 1

g_list = []

fav = input("What is your number 1 favorite PlayStation game? ")
g_list.append(fav)
fav = input("What is your number 2 favorite PlayStation game? ")
g_list.append(fav)
fav = input("What is your number 3 favorite PlayStation game? ")
g_list.append(fav)

for num, game in enumerate(g_list, 1):
    print(f"Your number {num} favorite game was {game}")