import math


frutas = ['banana', 'uva', 'laranja']
for fruta in frutas:
    print(fruta)


a = 1
b = 1
if a == b: print("a é igual a b")

for i in range(4):
    print(i)

soma = sum([1,2,3])
print(soma)

print("=-=-=-=-=-=-=-=-=-=")
a = 0
b = 1
while b > 10:
    print(b)
    a = b 
    b = a + b

print(a, b)
print("=-=-=-=-=-=-=-=-=-=")
print("a é maior") if a > b else print("b é maior")
