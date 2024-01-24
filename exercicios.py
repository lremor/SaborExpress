
## x = float(input('Digite a coordenada X: \n'))
## y = float(input('Digite a coordenada Y: \n'))

## if x > 0 and y > 0:
##         print('Primeiro quadrante')
## elif x < 0 and y > 0:
##         print('Segundo quadrante')
## elif x < 0 and y < 0:
##         print('Terceiro quadrante')
## elif x > 0 and y < 0:
##         print('Quarto quadrante')
## else:
##         print('O ponto esta localizado no eixo ou origem')


## idade = int(input('Qual sua idade? \n'))

## if idade <= 12 and idade >= 0:
##     print('Criança: 0 a 12 anos')
## elif idade >= 13 and idade <= 18:
##     print('Adolescente: 13 a 18 anos')   
## else:
##     print('Adulto: acima de 18 anos')


## usuario_correto = "alura"
## senha_correta = "alura123"

## usuario = input("Digite o nome de usuário: ")
## senha = input("Digite a senha: ")

## if usuario == usuario_correto and senha == senha_correta:
##     print("Login bem sucedido!")
## else:
##     print("Credenciais inválidas. Tente novamente.")


lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_nome = ['Luís', 'Liana', 'Gabi', 'Cristine']
lista_ano = [1990,2024]
pares = []
impares = []

for num in lista_num:
    print(f'{num}')
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
soma_dos_impares = sum(impares)
lista_num.sort(reverse=True)

print(f'{lista_num}')
print(f'Nomes: {lista_nome}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')
print(f'Soma dos ímpares: {soma_dos_impares}')

tabuada = int(input('Digite um numero \n'))
for numero in range(11):
    resultado = tabuada * numero
    print(f'{tabuada} X {numero} = {resultado}')
