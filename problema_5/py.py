def string_invertida(texto):

  string_invertida = ""
  for i in range(len(texto) - 1, -1, -1):
    string_invertida += texto[i]
  return string_invertida

texto_original = input('Digite a palavra ou frase que deseja que seja invertida \'-\' > .-.: ')

texto_invertido = string_invertida(texto_original)
print('***************************************************************')
print(f'String invertida: {texto_invertido}')