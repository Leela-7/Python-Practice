binary=input("Enter a binary number: ")

decimal=0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print("The decimal equivalent is:", decimal)  # Print the decimal equivalent
