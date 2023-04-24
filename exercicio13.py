numInt = int(input("Digite um numero inteiro: "))

divisao = numInt % 3
divisao2 = numInt % 7

if (divisao == 0) and (divisao2 == 0):
    print("Esse número é divisível por 3 e 7!")

else:
    print("Esse número não é divisível por 3 e 7.")
