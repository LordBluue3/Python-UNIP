import math
#Entrada de dados
lightning = int(input("Digite o raio: "))
height = int(input("Digite a altura: "))
#Processamento
volume = math.pi * (lightning**2)*height
#Saida
print("O volume da lata de óleo é: %.2f"%volume)