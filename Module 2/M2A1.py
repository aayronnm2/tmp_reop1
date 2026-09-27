# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 2 Assignment 1

g_list = []

favgame = input("What is your favorite game? ")
g_list.append(favgame.title())
favgame2 = input("What is your second favorite game? ")
g_list.append(favgame2.title())
favgame3 = input("What is your third favorite game? ")
g_list.append(favgame3.title())

print(f"One of your favorite games is {g_list.pop()}")
print(f"One of your favorite games is {g_list.pop()}")
print(f"One of your favorite games is {g_list.pop()}")