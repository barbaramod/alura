vendas22 = float(input('Quantidade de vendas de 2022: '))
vendas23 = float(input('Quantidade de vendas de 2023: '))
variacao = ((vendas23 - vendas22) / vendas22) * 100

if variacao > 20:
  sugestao = 'bonificação ao time de vendas'
elif 2 < variacao <= 20:
  sugestao = 'pequena bonificação ao time de vendas'
elif -10 < variacao <= 2:
  sugestao = 'planejamento de políticas de incentivo às vendas'
else:
  sugestao = 'corte de gastos'

print(f'Variação: {variacao:.2f}%\nSugestâo: {sugestao}.')
