"""
lista = [1,4,5,7,6,2]
print("lista =", lista)
ordlista = sorted(lista)
print(ordlista)
lista.sort()
print(lista)

tabela = {"Arroz": 0.5 , "Batata": 0.2 , "Carne" : 0.1}
tabela["Arroz"] = 7
#print(tabela["Arroz"])
"""

listacpf = [1, 4 ,56 ,7 ,86, 5, 63, 52]
cpf = 5 
cpf = int(input("Digite o Cpf: "))
achou = False
x=0

while x < len(listacpf):
    if listacpf[x] == cpf:
        achou = True
        break
    x += 1

if achou == True:
    print(f"ACHOU O {cpf} !!!!!!!!")
    input()
else:
    print("NÃO ACHOU!!!!!!!!")
    input()

