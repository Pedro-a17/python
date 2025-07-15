def div(k, j):
  if (j != 0):
    return k // j
  else:
    return "Error -> division by zero"

def count(num = 11, char = "#"):
  for i in range(1, num):
    print(char)

if __name__ == '__main__':
  a = int(input("type a number: "))
  b = int(input("type another number: "))

  result = div(a, b)
  print(f'{a} divided by {b} is: {result} ')

  count(3, "^")

# recursion

def factorial(num):
  if (num == 0 or num == 1):
    return 1
  elif (num < 0):
    return "not possible"
  else:
    return num * factorial(num - 1)

if __name__ == '__main__':
  x = int(input(":"))
  r = factorial(x)
  print(r)
  
