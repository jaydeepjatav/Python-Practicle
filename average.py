#input the length of list
length = int(input("Enter the number of Elements in the list: "))
nos = []
print("Enter the Elements:")

for i in range(length):
    number = float(input("Element: "))
    nos.append(number)

average = sum(nos) / length
print(f"Average of the list numbers is: {round(average, 3)}")
