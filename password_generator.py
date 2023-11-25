import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to PyPassword Generator!.")
num_letters=int(input("How many Letters would you like to have? : "))
num_numbers=int(input("How many Numbers would you like to have? : "))
num_symbols=int(input("How many Symbols would you like to have? : "))
password_list=[]
for char in range(1,num_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,num_numbers+1):
    password_list.append(random.choice(numbers))
for char in range(1,num_symbols+1):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print(f"Here is your new password : {password}")


