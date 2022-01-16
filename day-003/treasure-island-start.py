print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bem-vindo à Ilha do Tesouro")
print("Sua missão é encontrar o tesouro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print ("\nVocê está em uma encruzilhada. Onde você quer ir? ")

direcao = input("\n<================ Esquerda ou direita? ================>\n\n")
direcao = direcao.lower()

if direcao == "esquerda":
	lago = input("\nVocê chegou em um lago. Há uma ilha no meio do lago. Digite \"wait\" para esperar por um barco. Digite \"swim\" para nadar.\n\n")
	lago = lago.lower()
	
	if lago == "swim":
		ilha = input("\nVocê chega à ilha ileso. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe? vermelho, amarelo ou azul?\n\n")
		ilha = ilha.lower()

		if ilha == "vermelho":
			print("Queimado pelo fogo! Fim de jogo")
		elif ilha == "azul":
			print("Você entrou em uma sala de feras. Fim de jogo")
		elif ilha == "amarelo":
			print("Você encontrou o tesouro! Você venceu!")
		else:
			print("Fim de jogo.")

	else:
		print("Você foi atacado por uma truta irritada! Fim de jogo.")

else: 
	print("Você caiu em um buraco. Fim de jogo.")

