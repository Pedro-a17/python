dictionary = {
    "name" : "?",
    "age" : "19",
    "course" : "computer science"
}

print(dictionary)
dictionary["name"] = "Pedro"
print(dictionary)

print(f'name: {dictionary["name"]}')
print(len(dictionary), "elements")

dictionary["semester"] = "third"
print(dictionary["semester"])
print(dictionary)

del(dictionary["semester"])
print(dictionary)

print(dictionary.items())
for i in dictionary.items():
    print(i)

print(dictionary.keys())
for i in dictionary.keys():
    print(i)

print(dictionary.values())
for i in dictionary.values():
    print(i)

for key, value in dictionary.items():
    print(f'{key} : {value}')

dictionary.clear()
print(dictionary)

del(dictionary)
print(dictionary)
