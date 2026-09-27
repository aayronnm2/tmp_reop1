cities_list = ['los angeles', 'long beach', 'sacremento']
pop_list = [7000000, 500000, 600000]

for index, city in enumerate(cities_list):
    print(f"The city of {city} has a population of {pop_list[index]}")

cities_dict = {
    'los angeles': 7000000,
    'long beach': 500000,
    'sacramento': 600000
}
print("\n\n")

for city in cities_dict.keys():
    print(f"The city of {city} has a population of {cities_dict[city]}")

for values in cities_dict.items():
    print(f"{values}")

cities_dict['los angeles'] = 7500000
cities_dict['san francisco'] = 6250000

for city, pop in cities_dict.items():
    print(f"The city of {city} has a population of {pop}")

if 'fullerton' in cities_dict:
    print(f"The population of {'fullerton'} is {cities_dict.get('fullerton')}")
else:
    print(f"Fullerton not found")