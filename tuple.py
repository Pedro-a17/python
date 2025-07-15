t = (1, 2, 3 ,4 ,5)
t1 = (3, 4 ,5, 6 ,7)
tup = t + t1
print(tup)
print(len(t), sorted(t, reverse=True), max(t), min(t), sum(t), 1 in t, t.count(0))
list = list(tup)
list.append(0)
print(list)
