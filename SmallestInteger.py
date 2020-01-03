smallest = None
for value in [#insert list of integers here]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print(smallest)
