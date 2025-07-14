ß = "p"
A = 66.66
print("-", ß, "-", A)

print("changing line")
print("same line", end="")
print(" here")

formated_msg = "this is {0} and {1:.0f}".format(ß, A)
print(formated_msg)

print(f'{ß}, {round(A)}.')



