"""
    Programa "Hi _name_"

    Autor: Me Me Me (HW)
    Data: 12/04/2024
    Versão 0.1

    Descrição: professor, university, course, hours worked, hourly pay = 40 reais, tax 30%, print discounts, gross and net salary "
"""   
# Alocação de Memória 
hourly_pay = 40
tax = 0.3
discount = 0
gross_salary = 0
net_salary = 0

# Entrada de Dados
p_name = str(input("Nome do Professor: "))
u_name = str(input("Nome da Universidade: "))
c_name = str(input("Nome do Curso: "))
p_worked_hours = int(input(f"Quantidade de Horas Trabalhadas pelo Professor {p_name}: "))

# Processamento de Dados
gross_salary = p_worked_hours * hourly_pay
discount = gross_salary * tax
net_salary = gross_salary - discount

# Saída de Dados 
print (f' #####################################################',
        '                                      ',
        '     Nome do Professor:   
        '                                                      ',                                
        '     Nome da Universidade:                              ',
        '     Nome do Curso:                              ',
        '                                                      ',   
        '                                                      ',    
        '                                                      ',    
        '                                                      ',   
        '                                                      ',             
        ' #####################################################',sep='\n')
input ()