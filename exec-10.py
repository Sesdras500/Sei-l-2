# Entrada de dados
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

# Processamento
percentual_distribuidor = 28 / 100
percentual_impostos = 45 / 100

valor_distribuidor = custo_fabrica * percentual_distribuidor
valor_impostos = custo_fabrica * percentual_impostos

custo_final = custo_fabrica + valor_distribuidor + valor_impostos

# Saída de dados
print(f"O custo final ao consumidor é: R${custo_final:.2f}")
