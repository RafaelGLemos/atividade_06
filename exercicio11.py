nome = input("Digite seu Nome: ")
peso = float(input("Digite seu Peso em Kg: "))
altura = float(input("Informe sua Altura em m: "))

imc = peso / (altura**2)

if imc > 50:
    print(nome, " o Sr(a) está com Obesidade Mórbida")

elif imc > 35 and imc <= 50:
    print(nome, " o Sr(a) está com Obesidade")

elif imc > 25 and imc <= 35:
    print(nome, " o Sr(a) está com Excesso de peso", imc)

elif imc > 20 and imc <= 25:
    print(nome, " o Sr(a) está normal")

else:
    print(nome, " o Sr(a) está Abaixo do peso")
