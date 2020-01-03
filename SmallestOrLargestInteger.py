x = None
for value in [#insert list of integers here]:
    if x is None:
        x = value
    elif value < smallest: #the < symbol can be switched to > to flip the program and search for largest number!
        x = value
print(x)
