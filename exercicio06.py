nome = input("Digite seu nome: ")
nota_t = float(input("Digite a nota que você tirou no trabalho: "))
nota_p = float(input("Digite a nota que você tirou na prova: "))

media = (nota_t + nota_p) / 2

if media > 7:
    print(nome, " Aprovado")

else:
    print(nome, " Reprovado")
