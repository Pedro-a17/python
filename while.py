num = 0
m = []
while True:
    num = input("digite um número um \"x\" para parar:")
    if (num == "x" or num == "X"):
        break
    m.append(int(num))
    print(m)
print("fim")
