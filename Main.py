import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Bem-vindos ao criador de senhas!!!')
nr_letras = int(input('Quantas letras você quer na sua senha? \n'))
nr_numeros = int(input('Quantos números você quer na sua senha? \n'))
nr_simbolos = int(input('Quatos símbolos você quer na sua senha? \n'))

# #Criador de senhas fácil
# senha = ''
# for char in range(0, nr_letras):
#     senha += random.choice(letras)
# for char in range(0, nr_numeros):
#     senha += random.choice(numeros)
# for char in range(0, nr_simbolos):
#     senha += random.choice(simbolos)
#
# print(senha)

#Criador de senhas difícil
senha = []
for char in range(nr_letras):
    senha.append(random.choice(letras))
for char in range(nr_numeros):
    senha.append(random.choice(numeros))
for char in range(nr_simbolos):
    senha.append(random.choice(simbolos))

print(senha)
random.shuffle(senha)
print(senha)

senha_final = ''
for char in senha:
    senha_final += char
print(f'Sua senha é: ', senha_final)