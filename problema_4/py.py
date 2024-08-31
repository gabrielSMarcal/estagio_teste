import json

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

# Pega valores contidos no dicionário acima e organiza em um arquivo .json
with open ('faturamento.json', 'w') as arquivo:
    json.dump (faturamento, arquivo)

# Calcula o faturamento total
faturamento_total = sum (faturamento.values())

# Calcula e imprime o percentual de representação de cada estado
print ('Percentual de representação por estado:')
for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print (f'{estado}: {percentual:.2f}%')