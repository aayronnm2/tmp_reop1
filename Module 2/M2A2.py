# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']

print(f"Here are the top Sega games:")

for word in g_list:
    print(word)

removed_game = input("Which one do you think should be removed? ")
g_list.remove(removed_game)

print(f"Here are the new top Sega games:")

for word in g_list:
    print(word)