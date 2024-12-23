# Taking inputs
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))

# Calculating area and perimeter
area = l * b
perimeter = 2 * (l + b)

# Printing the results
print(f"Perimeter of the rectangle is: {round(perimeter, 3)}")
print(f"Area of the rectangle is: {round(area, 3)}")
