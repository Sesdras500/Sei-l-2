# Entrada de dados
salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste (em %): "))

# Processamento
reajuste = salario_atual * (percentual_reajuste / 100)
novo_salario = salario_atual + reajuste

# Saída de dados
print(f"O novo salário é: R${novo_salario:.2f}")
