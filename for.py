list = ["apple", "strawberry", "orange", "watermelon"]
l = []

for i in range(len(list)):
    l.append(list[i])
    if (i == 0):
        print(f'1 fruit:')
    else:
        print(f'{i + 1} fruits:')
    for x in l:
        print(f'{x.capitalize()}')
