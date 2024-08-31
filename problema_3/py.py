import json

def analisar_faturamento(dados_faturamento):

  faturamento_valido = [faturamento for faturamento in dados_faturamento if faturamento > 0]
  menor_faturamento = min(faturamento_valido)
  maior_faturamento = max(faturamento_valido)

  soma_faturamento = sum(faturamento_valido)
  media_mensal = soma_faturamento / len(faturamento_valido)

  dias_acima_da_media = sum(1 for faturamento in faturamento_valido if faturamento > media_mensal)

  return menor_faturamento, maior_faturamento, dias_acima_da_media

# Carregando os dados de faturamento a partir de um arquivo JSON;
with open('exemplo.json', 'r') as arquivo:
    dados = json.load(arquivo)
    faturamento_diario = dados['faturamento_diario']

# Analisando o faturamento;
menor_valor, maior_valor, dias_acima_media = analisar_faturamento(faturamento_diario)

# Retorno com os resultados;
print(f'Menor faturamento diário: R$ {menor_valor:.2f}')
print(f'Maior faturamento diário: R$ {maior_valor:.2f}')
print(f'Dias com faturamento acima da média mensal: {dias_acima_media}')