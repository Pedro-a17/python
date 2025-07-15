prime = {2, 3, 5, 7, 11}
print(2 in prime)
print(2 not in prime)
print(prime)

prime = [2, 3, 5, 7, 11, 11]
print(prime, end='')
prime_set = set(prime)
print(prime_set)

# union - intersection - symetric difference -
elements1 = {"H", "Br", "Ni", "Au"}
elements2 = {"H", "Au", "He", "Fl", "Zi", "Na"}
print(elements1 != elements2)
print(f'set union: {elements1 | elements2}')
print(elements1.union(elements2))
print(f'set intersection: {elements1 & elements2}')
print(elements1.intersection(elements2))
print(f'set symetric difference: {elements1 ^ elements2}')
print(elements1.symmetric_difference(elements2))

elements1.add("Cl")
elements1.remove("H")
elements1.remove("Ni")
elements1.pop()
print(elements1)

elements1.clear()
print(elements1)

elements1.discard("Na")

elements1.remove("Na")
