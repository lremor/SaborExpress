
import os

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

## ---------------------------------------------------------

# lista_num = [1,2,3,4,5,6,7,8,9,10]
# lista_nome = ['Luís', 'Liana', 'Gabi', 'Lelo']
# lista_ano = [1990,2024]
# pares = []
# impares = []

# def testetry():
#     try:
#         media = soma_de_todos / len(lista_num)
#         print('A média de todos é:',media)
#     except:
#         print('A lista esta vazia')

# for num in lista_num:
#     print(f'{num}')
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)
# soma_dos_impares = sum(impares)
# soma_de_todos = sum(impares+pares)
# lista_num.sort(reverse=True)

# print(f'{lista_num}')
# print(f'Nomes: {lista_nome}')
# print(f'Lista de pares: {pares}')
# print(f'Lista de ímpares: {impares}')
# print(f'Soma dos ímpares: {soma_dos_impares}')
# print(f'Soma de todos: {soma_de_todos}')
# testetry()

# tabuada = int(input('\nDigite um numero \n\n'))
# for numero in range(11):
#     resultado = tabuada * numero
#     print(f'{tabuada} X {numero} = {resultado}')

# ---------------------------------------------------------

dados_pessoa = [{
    'nome':'Luís', 
    'idade':33, 
    'cidade':'Erechim'
    }]

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal! ')
    main()

def subtitulo(texto):
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def alterar_idade():
    subtitulo('Alterando a idade')  
    nome_da_pessoa = input('Digite o nome da pessoa que deseja alterar a idade: \n\n')
    for pessoa in dados_pessoa:
        if nome_da_pessoa == pessoa['nome']:
            idade_pessoa = int(pessoa['idade'])
            print(f'\nA idade de {nome_da_pessoa} é {idade_pessoa} anos')
            nova_idade = float(input(f'\nDigite a nova idade de {nome_da_pessoa}: \n\n'))
            pessoa['idade'] = nova_idade
            idade_pessoa = int(pessoa['idade'])             
            print(f'\nA nova idade de {nome_da_pessoa} é {idade_pessoa} anos\n')
            adicionar_profissao()
        else:
            print('\nEsse nome não existe!\n')
            alterar_idade()

def adicionar_profissao():
    subtitulo('Adicionando uma profissão')
    nome_da_pessoa = input('Digite o nome da pessoa que deseja adicionar a profissão: \n\n')
    for pessoa in dados_pessoa:
        if nome_da_pessoa == pessoa['nome']:
            profissao = input(f'\nDigite o nome da profissão de {nome_da_pessoa}: \n\n')
            pessoa['profissao'] = profissao
            print(f'\nA profissão {profissao} foi adicionada ao usuário {nome_da_pessoa}')
            profissao_atualizada = pessoa['profissao']
            print(f'\nA profissão de {nome_da_pessoa} agora é {profissao_atualizada}')
            voltar_ao_menu_principal()

        else:
            print('\nEsse nome não existe!\n')
            adicionar_profissao()
        

def main():
    os.system('cls')
    alterar_idade()

if __name__ == '__main__':
    main()