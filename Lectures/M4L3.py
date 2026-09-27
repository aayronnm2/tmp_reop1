student1_dict = {
    'name': 'Jim Bob',
    'id': 123456,
    'schedule': ['CPSC223p', 'ENG1', 'MATH2']
}

for myclass in student1_dict.get('schedule'):
    print(f"The class is {myclass}")


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word]+1
    else:
        frequency[word] = 1


for word, count in frequency.items():
    print(f"{word}: {count}")