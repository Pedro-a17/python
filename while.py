num = 0
m = []

while (num <= 10):
  print(num ** 2)
  num += 1
print("end")

while True:
  num = input("type an int number or \"x\" to stop ")
  if (num == "x" or num == "X"):
    break
  m.append(int(num))
  print(m)
print("end")
  
