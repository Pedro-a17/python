docstring = """suitable string for python documentation
, respects offset and supports multiple lines"""
print(docstring)

string = "    the void    "
email = input("type your e-mail: ")

s = string.split()
for l in s:
  print(l)
  
at = email.find("@")
public = email[:at]
domain = email[at:]
print(email, public, domain)
replace = email.replace(public, "pedrosilveira1704")
print(replace)
print("1704" in email)
print("1704" in replace)

print(string.lstrip())
print(string.rstrip())
print(string.strip())

print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())

string2 = "idk"

print(string2.capitalize())

print(string2.ljust(5, "-"))
print(string2.rjust( 5, "-"))
print(string2.center(5, "-"))

print(string2.startswith("i"))
print(string2.endswith("P"))
