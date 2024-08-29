# Passo 1: Solicitar ao usuário que digite a idade em anos
anos = int(input("Digite a idade em anos: "))

# Passo 2: Solicitar ao usuário que digite a idade em meses
meses = int(input("Digite a idade em meses: "))

# Passo 3: Solicitar ao usuário que digite a idade em dias
dias = int(input("Digite a idade em dias: "))

# Passo 4: Calcular o total de dias
total_dias = (anos * 365) + (meses * 30) + dias

# Passo 5: Exibir o total de dias
print(f"A idade em dias é {total_dias}")
