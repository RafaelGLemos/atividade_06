hrAula = float(input("Informe o valor da hora aula: "))
qtAula = int(input("Informe a quantidade de aula dada no mês: "))
desInss = float(input("Informe o percentual do seu INSS: "))

desInss = (hrAula * qtAula) * (desInss/100)

salario = (hrAula * qtAula) - desInss

if salario >= (1302 * 10):
    print("Sortudo!", salario)

elif salario >= (1302 * 6) and salario <= (1302 * 9):
    print("Um dia você chega lá!", salario)

else:
    print("Ah! Coitado!", salario)
