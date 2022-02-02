# importing random module
import random

# list of letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# welcome message and user inputs
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# simple password generator (order not randomized)
simple_password = ""

for i in range(int(nr_letters)):
    simple_password += random.choice(letters)
for i in range(int(nr_symbols)):
    simple_password += random.choice(symbols)
for i in range(int(nr_numbers)):
    simple_password += random.choice(numbers)

print(f"The simple version of your password is: {simple_password}")

# complicated password generator (order randomized)
complicated_password_list = []

for i in range(int(nr_letters)):
    complicated_password_list.append(random.choice(letters))
for i in range(int(nr_symbols)):
    complicated_password_list.append(random.choice(symbols))
for i in range(int(nr_numbers)):
    complicated_password_list.append(random.choice(numbers))

random.shuffle(complicated_password_list)

complicated_password = "".join(complicated_password_list)
print(f"The complicated version of your password is: {complicated_password}")