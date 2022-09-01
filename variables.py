from turtle import width
from xmlrpc.client import Boolean


name = "Diana"
age = 20
wage = 2000.00
booleanTrue = True
booleanFalse = False

print(name,age,wage)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Digite a primeira nota")
fristNumber = int(input())

print("Digite a segunda nota")
secondNumber = int(input())

average = (fristNumber + secondNumber)/2

print (int(average))

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Digite um numero")
number = int(input())
if 1 == number:
    print('Este numero é igual a "1"?',booleanTrue)
else:
    print('Este numero é igual a "1"?',booleanFalse)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

print("Entre com a altura:")
height = int(input())

print("Entre com a largura:")
width = int(input())

area = (height * width)/2
print("Área do triangulo: ",area) 

