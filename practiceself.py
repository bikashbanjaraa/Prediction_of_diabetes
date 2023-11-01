def add(*args):
    total = 0 
    for item in args:
        total = total + item 
    return total

result = add (1,2,3,4,5)
print(result)
