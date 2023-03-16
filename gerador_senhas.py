import string
import random

def gLetras(i):
    print("Gerando senha ", i+1)
    letras = int(input("Diga o total de letras que deve conter na senha: "))
    letras_s = random.SystemRandom().choices(string.ascii_letters, k = letras)
    return letras_s

def gNumeros():
    cesc = int(input("Diga o total de caracteres especiais que deve conter na senha: "))
    cesp = random.SystemRandom().choices(string.punctuation, k = cesc)
    return cesp

#main

senha = []
totalsenhas = int(input("Diga o total de senhas que você quer gerar: "))
for i in range(totalsenhas):
    senhaauxl = gLetras(i)
    senhaauxn = gNumeros()
    aux_senha = senhaauxl+senhaauxn
    random.shuffle(aux_senha)
    sesp = ''.join(aux_senha)
    senha.append(sesp)

for i in range(0, totalsenhas):
   print("A senha", i+1, "é:",senha[i])