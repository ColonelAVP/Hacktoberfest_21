# fn to generate fibonacci numbers upto a given range
def fibonacci_Series(upto):
    fibonacci_list = []
    x = 0
    y = 1
    while x < upto:
        fibonacci_list.append(x)
        x, y = y, x+y
    return fibonacci_list

# Driver's Code
print(fibonacci_Series(100))