print("Escolha a operação que deseja realizar com os dois números:")
print("- par ou ímpar")
print("- positivo ou negativo")
print("- inteiro ou decimal")
operacao = input("Informe a operação: ").lower()
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if operacao == 'par ou ímpar':
  if num1 % 2 == 0:
    print(f'O número {num1} é par.')
  else:
    print(f'O número {num1} é ímpar.')
  if num2 % 2 == 0:
    print(f'O número {num2} é par.')
  else:
    print(f'O número {num2} é ímpar.')
elif operacao == 'positivo ou negativo':
  if num1 > 0:
    print(f'O número {num1} é positivo.')
  else:
    print(f'O número {num1} é negativo.')
  if num2 > 0:
    print(f'O número {num2} é positivo.')
  else:
    print(f'O número {num2} é negativo.')
elif operacao == 'inteiro ou decimal':
  if num1 % 1 == 0:
    print(f'O número {int(num1)} é inteiro.')
  else:
    print(f'O número {num1} é decimal.')
  if num2 % 1 == 0:
    print(f'O número {int(num2)} é inteiro.')
  else:
    print(f'O número {num2} é decimal.')
else:
   print('Valor inválido! Digite uma das opções abaixo: \n- par ou ímpar\n- positivo ou negativo\n- inteiro ou decimal')
