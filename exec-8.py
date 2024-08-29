# Passo 1: Solicitar ao usuário que digite o número total de eleitores
total_eleitores = int(input("Digite o número total de eleitores: "))

# Passo 2: Solicitar ao usuário que digite o número de votos brancos
votos_brancos = int(input("Digite o número de votos brancos: "))

# Passo 3: Solicitar ao usuário que digite o número de votos nulos
votos_nulos = int(input("Digite o número de votos nulos: "))

# Passo 4: Solicitar ao usuário que digite o número de votos válidos
votos_validos = int(input("Digite o número de votos válidos: "))

# Passo 5: Calcular o percentual de votos brancos
percentual_brancos = (votos_brancos / total_eleitores) * 100

# Passo 6: Calcular o percentual de votos nulos
percentual_nulos = (votos_nulos / total_eleitores) * 100

# Passo 7: Calcular o percentual de votos válidos
percentual_validos = (votos_validos / total_eleitores) * 100

# Passo 8: Exibir os percentuais
print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")
