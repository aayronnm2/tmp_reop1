# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 4 Assignment 4

guy_dict1 = {
    'name': 'Jimmer',
    'age': 23,
    'scout rank': 'Eagle',
    'scout badges': []
}

print(f"I know Jimmer has three scout badges, what are they?")
scoutBadges = []

badge = input("The first badge is: ")
scoutBadges.append(badge)
badge = input("The second badge is: ")
scoutBadges.append(badge)
badge = input("The third badge is: ")
scoutBadges.append(badge)

guy_dict1['scout badges'] = scoutBadges

print(f"{guy_dict1}")