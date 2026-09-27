# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 4 Assignment 3

games_dict = {}

for num in range(1,4):
    game = input("What is a great game? ")
    console = input("What system can I play that on? ")
    games_dict[game] = {console}

print("That's too many, let's get rid of one")
games_dict.pop(input("What game should we remove? "))
print("The new dictionary is:")

for game, console in games_dict.items():
    print(f"You can play {game} on {list(console)[0]}")