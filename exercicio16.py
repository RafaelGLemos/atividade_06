falta = int(input("DIgite o Número de faltas que teve no semestre: "))
nota1 = float(input("Digite o valor da primeira prova: "))
nota2 = float(input("Digite o valor da segunda prova: "))

media = (nota2 + nota1) / 2

if falta >= 32:
    print("Reprovado por falta")

elif media >= 7:
    print("Aprovado ", media)

else:
    print("Reprovado ", media)

print("A média para passar de ano são no mínimo 7 pontos e 31 faltas.")
