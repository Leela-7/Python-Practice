import math
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")
