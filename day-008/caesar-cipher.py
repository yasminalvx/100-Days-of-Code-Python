alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, direction):
	end_text = ""
	if direction == "decodificar":
		shift_amount *= -1
	for letter in start_text:
		if letter in alphabet:
			position = alphabet.index(letter)
			new_position = position + shift_amount % 26
			end_text += alphabet[new_position]
		else:
			end_text += letter
	if direction == "decodificar":
		print (f"O texto decodificado é {end_text}")
	elif direction == "codificar":
		print (f"O texto codificado é {end_text}")

from art import logo
print(logo)

should_end = False
while not should_end:

  direction = input("Digite 'codificar' para criptografar, Digite 'decodificar' para descriptografar:\n")
  text = input("Digite sua mensagem:\n").lower()
  shift = int(input("Digite o número do pulo:\n"))

  caesar(start_text=text, shift_amount=shift, direction=direction)

  restart = input("Digite 'sim' se quiser tentar novamente. Caso contrário, digite 'não'.\n")
  if restart == "não":
    should_end = True
    print("Adeus!")