tipo = input('Informe o tipo de combustível (E ou D): ').upper()
qntLitro = float(input('Digite a quantidade de litros: '))
precoL = 0
desconto = 0

if tipo == 'E':
  precoL = 1.70
  if qntLitro <= 15:
    desconto = (precoL * qntLitro * 0.02)
  else:
    desconto = (precoL * qntLitro * 0.04)
elif tipo == 'D':
  precoL = 2
  if qntLitro <= 15:
    desconto = (precoL * qntLitro * 0.03)
  else:
    desconto = (precoL * qntLitro * 0.05)
else:
  print('Valor inválido! Informe E para etanol ou D para diesel.')

if precoL != 0:
  valor = ((precoL * qntLitro) - desconto)
  print(f'- Combustível: {tipo}\n- Litro: {qntLitro:.2f} L\n- Preço do litro: R$ {precoL:.2f}/L\n- Desconto: R$ {desconto:.2f}')
  print(f'Valor a ser pago: R$ {valor:.2f}.')
