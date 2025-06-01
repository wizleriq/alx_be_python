size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    # Use for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")  # stay on the same line
    print()  # move to the next line after each row
    row += 1