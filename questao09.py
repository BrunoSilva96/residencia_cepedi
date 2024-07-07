salario_mensal = int(input("Digite seu salário para calcular sei imposto de renda: "))

salario_anual = salario_mensal * 12
salario_anual_minimo_para_imposto = 28559.70

if (salario_anual > salario_anual_minimo_para_imposto):
  print(f"Seu salário ultrapassou o valor de {salario_anual_minimo_para_imposto}, totalizando {salario_anual}, logo você terá que contribuir com o governo.")
else:
  print("Seu salário ainda não atingiu o valor mínimo para contribuição com imposto de renda.")