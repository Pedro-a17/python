#listas -

l1 = [1, 2 ,3]
l2 = [4, 5 ,6]
l1[-1], l1[0] = 4, 0
l = l1 + l2
print(l[0: 2])
print(l)
l.append(6)
l.pop(1)
print(l)
l.insert(2, 2)
print(l, len(l))
l_sort = sorted(l, reverse=True)
print(l_sort)
print(max(l), min(l), sum(l))
print(7 in l)
