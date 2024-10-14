def print_odd_number(n):
    for i in range(1, n+1, 2):
        print(i, end=" ")

n = int (input("enter the value of n: "))
print ("Odd numbers up to", n, ":")
print_odd_number(n) 