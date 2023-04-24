salario = float(input("Digite seu Salário: "))
financiamento = float(input("Digite o valor que deseja financiar: "))

if financiamento <= (salario * 5):
    print("Financiamento Concedido")

else:
    print("Financiamento Negado")

print("Obrigado por nos consultar.")
