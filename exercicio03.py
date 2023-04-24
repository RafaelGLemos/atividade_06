p1 = float(input("Digite a pontuação 1: "))
p2 = float(input("Digite a pontuação 2: "))
p3 = float(input("Digite a pontuação 3: "))

if p1 > p2 and p2 > p3:
    print("primeiro colocado: " + str(p1))
    print("Segundo colocado: " + str(p2))
    print("Terceiro colocado: " + str(p3))

elif p1 > p3 and p3 > p2:
    print("primeiro colocado: " + str(p1))
    print("Segundo colocado: " + str(p3))
    print("Terceiro colocado: " + str(p2))

elif p2 > p1 and p1 > p3:
    print("primeiro colocado: " + str(p2))
    print("Segundo colocado: " + str(p1))
    print("Terceiro colocado: " + str(p3))

elif p2 > p3 and p3 > p1:
    print("primeiro colocado: " + str(p2))
    print("Segundo colocado: " + str(p3))
    print("Terceiro colocado: " + str(p1))

elif p3 > p2 and p2 > p1:
    print("primeiro colocado: " + str(p3))
    print("Segundo colocado: " + str(p2))
    print("Terceiro colocado: " + str(p1))


else:
    print("primeiro colocado: " + str(p3))
    print("Segundo colocado: " + str(p1))
    print("Terceiro colocado: " + str(p2))
