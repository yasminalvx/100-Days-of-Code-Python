import random
from hangman_art import stages, logo
from hangman_words import word_list

points = 0

def str_word_hidden(word_hidden):
	str_result = ""

	for i in range(0, len(word_hidden)):
		str_result += word_hidden[i]

	return str_result

game_is_finished = False

chosen_word = random.choice(word_list)
word_hidden = []

for i in range(0, len(chosen_word)):
	word_hidden.append('-')

while not game_is_finished:
	print('\033c')
	print (logo)
	print(f"{stages[points]}     {' '.join(word_hidden)}")

	guess = input("\nAdvinhe uma letra: ").lower()

	if guess in word_hidden:
		input(f"Você já chutou a letra \'{guess}\'. (Digite ENTER)")

	guessed = False

	for i in range(0, len(chosen_word)):
		if chosen_word[i] == guess:
			print(word_hidden[i])
			word_hidden[i] = guess
			guessed = True
	
	if guessed == False:
		input(f"Você chutou \'{guess}\' e não está na palavra. Você perdeu um ponto (Digite ENTER)")
		points += 1

	if points == 6:
			game_is_finished = True
			print('\033c')
			print (logo)
			print(f"{stages[points]}     {' '.join(chosen_word)}")
			print("\nVocê perdeu! Fim de jogo.")

	if not "-" in word_hidden:
		print('\033c')
		print (logo)
		print(f"{stages[points]}     {' '.join(chosen_word)}")
		print("\nVocê venceu! Parabéns!")
		game_is_finished = True

	