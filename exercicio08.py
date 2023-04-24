salario = float(input("Informe seu salário: "))

if salario < 500:
    reajuste = (salario * 1.15)
    print(reajuste, " Esse é seu salário reajustado.")

elif salario >= 500 and salario <= 1000:
    reajuste = (salario * 1.10)
    print(reajuste, " Esse é seu salário reajustado.")

else:
    reajuste = (salario * 1.05)
    print(reajuste, " Esse é seu salário reajustado.")
