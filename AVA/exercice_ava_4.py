tabuada = int(input("Qual tabuada você deseja descobrir?: "))
resultado = 0;
for x in range(0, 11):
    resultado = x * tabuada
    print (x,"X",tabuada,"=",resultado)