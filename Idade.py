idade = int(input("\nQuantos anos você tem?"));
if idade >= 123:
    result ="Jamais na história alguém viveu tanto como você. Estou com medo... O_O" 
elif idade >= 60:
    result = "Parabéns!! Você é um Idoso."
elif idade >= 18:
    result = "Você é um Adulto"    
else:
    result = "Você é menor de idade."
print (result)
input ()