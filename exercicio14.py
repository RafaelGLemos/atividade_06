salario = float(input("Digite seu Salário bruto: "))
prestacao = float(input("Digite o valor da prestação que deseja pagar: "))

if prestacao > salario*0.3:
    print("Você não pode pegar o empréstimo.")

else:
    print("Você pode pegar o empréstimo!")
