def calcular_valor_conta(kw_consumidos, bandeira):
  preco_kwh = 0.56
  valor_geracao = 0.41
  valor_imposto = 0.2252

  if bandeira == 1:
    bandeira_vigente = 0.015
  elif bandeira == 2:
    bandeira_vigente = 0.040
  elif bandeira == 3:
    bandeira_vigente = 0.060
  else:
    raise ValueError("Tarifa inválida. favor escolher 1, 2 ou 3.")

  consumo_kwh_bruto = kw_consumidos * preco_kwh

  valor_parcial_consumo = consumo_kwh_bruto + (kw_consumidos * valor_geracao) + (kw_consumidos * valor_imposto)
  valor_total_consumo = valor_parcial_consumo + (kw_consumidos * bandeira_vigente)

  return valor_total_consumo

consumo_mensal_kw = int(input("Qual foi o consumo de Kw/h no periodo de 1 mês?"))

print("Selecione a bandeira tarifária em vigor:")
print("1 - Amarela R$ 0,015")
print("2 - Bandeira vermelha - Patamar 1 R$ 0,040")
print("3 - Bandeira vermelha - Patamar 2 R$ 0,060")
bandeira_vigor = int(input("Digite o número correspondente à bandeira tarifária: "))

valor_total = calcular_valor_conta(consumo_mensal_kw, bandeira_vigor)

print(valor_total)