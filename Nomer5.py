def print_design(n):
    for i in range(1, n+1):  # Loop through 1 to n
        print(f"{i} " * i)  # Print 'i' repeated 'i' times followed by a space

# Example usage:
n = int(input("Enter the value of n: "))
print_design(n)
