"""
    Programa "Hello World"

    Autor: Me Me Me (HW)
    Data: 12/04/2024
    Versão 0.1

    Descrição: print "Hello World"
"""   
# Alocação de Memória
message = "input"
print_message = "output" 

# Entrada de Dados
message = str(input('\nEscreva "Hello World" para printálo: '))

# Processamento de Dados
if message == str("Hello World") or str('"Hello World"'):
    print_message = message
else:
    print_message = 'Algo que não é "Hello World" :( '

# Saída de Dados
print (f"Você Declarou: {print_message}!")
input ()