#Espaço para logo
from art import logo

#Funções da Calculadora
def soma(n1, n2):
	return float(n1) + float(n2)

def subtracao(n1, n2):
	return float(n1) - float(n2)

def multiplicacao(n1, n2):
	return float(n1) * float(n2)

def divisao(n1, n2):
	return float(n1) / float(n2)

operacoes = {
	"+": soma,
  	"-": subtracao,
  	"*": multiplicacao,
  	"/": divisao
}

def calcular (n1, n2, operador):
	funcao_operacao = operacoes[operador]
	return funcao_operacao(n1, n2)

#Funcionamento da Calculadora
print(logo)

n1 = input("Qual o primeiro valor? ")
print(" + - * / ")
operacao = input("Escolha uma operação: ")
n2 = input("Qual o segundo valor? ")

resultado = calcular(n1, n2, operacao)

print(f"{n1} {operacao} {n2} = {resultado}")

recalcular = input ("\nDeseja fazer outro cálculo com esse valor (s/n)? ").lower()
if (recalcular == 's'):
	continuar = True
else:
	continuar = False

while continuar:
	n1 = resultado
	print('\033c')
	print(logo)
	print(f"Valor atual: {resultado}")
	print(" + - * / ")
	operacao = input("Escolha uma operação: ")
	n2 = input("Qual o segundo valor? ")

	resultado = calcular(n1, n2, operacao)

	print(f"{n1} {operacao} {n2} = {resultado}")

	recalcular = input ("\nDeseja fazer outro cálculo com esse valor (s/n)? ").lower()
	if (recalcular == 's'):
		continuar = True
	else:
		continuar = False

print("\nCalculadora finalizada!")