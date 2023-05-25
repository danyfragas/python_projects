from random import choice
import string

tamanho = int(input('Informe o tamanho desejável da sua senha: '))
caracteres = string.ascii_letters + string.digits + string.punctuation
# caracteres minúsculos, maiúsculos e especiais

nova_senha = ''
for i in range(tamanho):
    nova_senha += choice(caracteres)

print(f'A senha gerada é: {nova_senha}')
