import string
import random

# Get the desired length of the password from the user
length = int(input("Enter the Length of Password: "))

# Generate the password
password = ""
for i in range(length):
    password += random.choice(string.ascii_letters + string.digits + string.punctuation)

# Print the generated password
print(f"Generated Password: {password}")
