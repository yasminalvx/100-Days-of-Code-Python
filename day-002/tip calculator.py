print("====================================") 
print("Bem-vindo a Calculadora de Gorjetas!")
print("====================================") 

total_conta = float(input("\nQual foi o valor total da conta? R$ "))
perc_gorjeta = input("Quanto de gorjeta deseja pagar? 10, 12 ou 15? ")
qtd_pessoas = int(input("Quantas pessoas vão dividir a conta? "))

perc_gorjeta = float("1." + perc_gorjeta)

valor_final = round((total_conta/qtd_pessoas)*perc_gorjeta, 2)

print(f"Cada pessoa vai pagar: R$ {valor_final:.2f}")