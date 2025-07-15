def div(x, y):
  return round(x / y, 2)

if __name__ == '__main__':
  while True:
    try:
      n1 = int(input("type a number: "))
      n2 = int(input("type a number: "))
      break
    except ValueError:
      print(f'an error occurred while reading the value, please try again')
  try:
    r = div(n1, n2)
  except ZeroDivisionError:
    print(f'division by zero is not possible')
  except:
    print(f'some error occurred')
  else:
    print(r)
  finally:
    print(f'\n end')

    
    
