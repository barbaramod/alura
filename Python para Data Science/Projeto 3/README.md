# Projeto 3 - Cálculo de Valor de Combustível com Desconto

## Descrição do Projeto
Este projeto cria um programa que calcula o valor a ser pago por um cliente ao comprar **etanol ou diesel**, aplicando descontos de acordo com a quantidade comprada.  

- Para **etanol**:  
  - Até 15 litros: desconto de 2% por litro  
  - Acima de 15 litros: desconto de 4% por litro  
- Para **diesel**:  
  - Até 15 litros: desconto de 3% por litro  
  - Acima de 15 litros: desconto de 5% por litro  

O preço do litro de diesel é **R$ 2,00** e o preço do litro de etanol é **R$ 1,70**.

---

## Extended Description
O objetivo deste projeto é praticar:  
- **Entrada de dados do usuário** (`input`)  
- **Estruturas condicionais** (`if`, `elif`, `else`)  
- **Operações matemáticas** com multiplicação e porcentagem  
- **Formatação de saída** com casas decimais  

O programa realiza os seguintes passos:  
1. Recebe do usuário o tipo de combustível (`E` para etanol ou `D` para diesel)  
2. Recebe a quantidade de litros vendidos  
3. Calcula o valor do desconto multiplicando preço, quantidade e taxa de desconto  
4. Calcula o valor total a ser pago subtraindo o desconto do valor bruto  
5. Exibe informações detalhadas do cálculo e valor final

---

## Funcionalidades
- Recebe tipo de combustível e quantidade de litros  
- Calcula desconto de acordo com regras definidas  
- Mostra o preço do litro, quantidade comprada, desconto e valor final  
- Trata entradas inválidas com mensagem de erro

---

## Como executar
1. Certifique-se de ter o Python instalado  
2. Execute o arquivo `combustivel_desconto.py`:

`
