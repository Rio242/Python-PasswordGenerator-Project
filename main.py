#Password Generator Project
import random # to get random function
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# need to create for loop to run through each list ie(letters, numbers,symbol) up to the number user choses
for letter in range(0,nr_letters):
  # need to create a function to pick a random list item at each instance
  # I refered to askpython random function documentation(https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences)
  l = random.sample(letters,nr_letters)

for number in range(0,nr_numbers):
  n = random.sample(numbers,nr_numbers)

for symbol in range(0,nr_symbols):
  s = random.sample(symbols,nr_symbols)

password = l+s+n # variable to concatenate lists

simple_pass = ''.join(password) # join function combines each list item
print(f"Your genereated password is: {simple_pass}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#random shuffle function to shuffle list items
random.shuffle(password) #used this shuffle function to completely randomize order of items in password variable

#print and join function
hard_pass = ''.join(password)
print(f"Your completely randomized genereated password is: {hard_pass}")

