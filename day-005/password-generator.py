#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao gerador de senhas!\n")
nr_letters= int(input("Quantas letras você gostaria de ter na sua senha?\n")) 
nr_symbols = int(input(f"Quantos símbolos você gostaria?\n"))
nr_numbers = int(input(f"Quantos números você gostaria?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

senha = ""

for i in range(nr_letters):
	senha += random.choice(letters)

for i in range(nr_symbols):
	senha += random.choice(symbols)

for i in range(nr_numbers):
	senha += random.choice(numbers)

# print(f"Sua senha gerada é: {senha}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for i in range(nr_letters):
	password_list.append(random.choice(letters))

for i in range(nr_symbols):
	password_list.append(random.choice(symbols))

for i in range(nr_numbers):
	password_list.append(random.choice(numbers))

random.shuffle(password_list)

senha = ""

for i in range(len(password_list)):
	senha += password_list[i]

print(f"Sua senha gerada é: {senha}")