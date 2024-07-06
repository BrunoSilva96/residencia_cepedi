contador = 3
lista_numeros = []

while contador > 0:
  numerosCrescente = int(input("Digite um número: "))
  lista_numeros.append(numerosCrescente)
  contador -= 1

lista_numeros.sort()

print(lista_numeros)
