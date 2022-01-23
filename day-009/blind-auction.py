from art import logo

others_users = True

bids = {}

while others_users:
	print(logo)

	name = input("Qual é o seu nome? ")
	bid = input("Qual é a sua oferta? R$ ")

	bids[name] = bid

	str_others_users = input("Há outras pessoas que querem fazer uma oferta? (Sim ou não) ").lower()
	if str_others_users == "não":
		others_users = False
	elif str_others_users == "sim":
		print('\033c')

greater = 0
win = ""

for bid in bids:
    if (int(bids[bid]) > int(greater)):
       greater = bids[bid]
       win = bid

print(f"O ganhador é {win} com RS {greater}")
