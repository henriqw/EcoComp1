"""

 Descrição do Programa: 

"""


# Alocação de Memória e Entrada de Dados
fatores = 3
parcela = 0
num = 0 
soma = 0

# Processamento de Dados
while (parcela < fatores):
    num = int(input(f"\nInforme a parcela {parcela + 1} "))
    soma = soma + num
    parcela += 1


# Saída de Dados
print (f"\n A soma das parcelas é {soma}.")
input ()