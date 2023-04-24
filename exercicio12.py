lado1 = float(input("Informe a medida de um lado do triangulo: "))
lado2 = float(input("Informe a medida de um lado do triangulo: "))
lado3 = float(input("Informe a medida da base do triangulo: "))

if (lado1 or lado2 or lado3) == 0:
    print("Não existe um triangulo com essas medidas: ")

elif (lado1 < lado2 + lado3) or (lado2 < lado1 + lado3) or (lado3 < lado2 + lado1):
    print("Não existe um triangulo com essas medidas: ")

elif lado1 == lado2 == lado3:
    print("Esse triâgulo é equilátero")

elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Esse triâgulo é isósceles")

else:
    print("Esse triângulo é escaleno")
