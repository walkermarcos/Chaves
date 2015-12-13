from mhlib import isnumeric
def verifica_cpf(cpf):
    numeros = ''
    for c in cpf:
        if isnumeric(c) or c == '0':
            numeros += c
    total1 = 0
    i = 10
    for n in numeros[:9]:
        total1 += (int(n) * i)
        i -= 1
    total2 = 0
    i = 11
    for n in numeros[:10]:         
        total2 += (int(n) * i)
        i -= 1
    resto1 = total1 % 11
    resto2 = total2 % 11
    if resto1 < 2: dig1 = 0
    else: dig1 = 11 - resto1
    if resto2 < 2: dig2 = 0
    else: dig2 = 11 - resto2
    if (dig1 == int(numeros[9])) and (dig2 == int(numeros[10])):
        return True 
    else: return False  

cpf = '123.456.789-45'
print verifica_cpf(cpf)
