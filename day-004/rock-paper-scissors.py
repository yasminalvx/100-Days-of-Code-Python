rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

pontuacao = [0, 0]

while True:
	choise = int(input('''Qual você escolhe? \n
0 - Pedra 
1 - Papel 
2 - Tesoura\n'''))

	if choise != 0 and choise != 1 and choise != 2:
		print("\nDesculpe, essa opção não existe! :(\nJogo finalizado.")
		break

	choise_computer = random.randint(0, 2)

	choises = [rock, paper, scissors]

	print("\nVocê: " + choises[choise])
	print("Computador: " + choises[choise_computer])

	if choise == 0 and choise_computer == 1:
		print("Papel embrulha a pedra. Você perdeu!")
		pontuacao[1] += 1
	elif choise == 0 and choise_computer == 2:
		print("Pedra quebra tesoura. Parabéns! Você venceu!")
		pontuacao[0] += 1
	elif choise == 1 and choise_computer == 0:
		print("Papel embrulha a pedra. Parabéns! Você venceu!")
		pontuacao[0] += 1
	elif choise == 1 and choise_computer == 2:
		print("Tesoura corta papel. Você perdeu!")
		pontuacao[1] += 1
	elif choise == 2 and choise_computer == 0:
		print("Pedra quebra tesoura. Você perdeu!")
		pontuacao[1] += 1
	elif choise == 2 and choise_computer == 1:
		print("tesoura corta papel. Parabéns! Você venceu!")
		pontuacao[0] += 1
	else:
		print("Você empatou")
		pontuacao[1] += 1
		pontuacao[0] += 1


	print(f"\nPlacar: Você {pontuacao[0]} x Computador {pontuacao[1]}")

	sair = input("\nPara sair digite 3: (ou ENTER para continuar) ")
	
	if sair == "3":
		print("\nObrigado por jogar! Até a próxima! :)")
		break
	else:
		print("\033[H\033[J", end="")
