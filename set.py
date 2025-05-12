#sets - conjuntos 
# -> coleção não ordenada de valores únicos - não suporta valores duplicados;
# mutáveis - embora não suportem modificações de itens, suportam adição de itens;
# suportam operações matemáticas sobre conjuntos
#:
primos = {2, 3, 5, 7, 11}
print(2 in primos)
print(2 not in primos)
print(primos)

primos = [2, 3, 5, 7, 11, 11]
print(primos, end='')
primos_set = set(primos)
print(primos_set)

elementos1 = {"H", "Br", "Ni", "Au"}
elementos2 = {"H", "Au", "He", "Fl", "Zi", "Na"}
print(elementos1 != elementos2)
print(f'união de conjuntos: {elementos1 | elementos2}')
print(elementos1.union(elementos2))
print(f'intersecção de conjuntos: {elementos1 & elementos2}')
print(elementos1.intersection(elementos2))
print(f'diferença simétrica de elementos: {elementos1 ^ elementos2}')
print(elementos1.symmetric_difference(elementos2))

elementos1.add("Cl")
elementos1.remove("H")
elementos1.remove("Na")
elementos1.discard("Na")
elementos1.pop()
elementos1.clear()
print(elementos1)
