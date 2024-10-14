def find_largest(a, b, c):
    if a >= b and a >= c:
        print (a)
    elif b >= a and b >= c:
        print (b)
    else:
        print (c)

# Example usage:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("The largest number is:", end="")
find_largest(a, b, c)
