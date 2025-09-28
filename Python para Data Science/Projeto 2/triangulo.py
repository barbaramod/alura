a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))

if a + b <= c or b + c <= a or a + c <= b: 
    print('Não forma um triângulo')
elif a == b == c:
    print('Triângulo equilátero')
elif a == b or b == c or a == c:
    print('Triângulo isósceles')
else:
    print('Triângulo escaleno')
