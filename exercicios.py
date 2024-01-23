
x = float(input('Digite a coordenada X: \n'))
y = float(input('Digite a coordenada Y: \n'))

if x > 0 and y > 0:
        print('Primeiro quadrante')
elif x < 0 and y > 0:
        print('Segundo quadrante')
elif x < 0 and y < 0:
        print('Terceiro quadrante')
elif x > 0 and y < 0:
        print('Quarto quadrante')
else:
        print('O ponto esta localizado no eixo ou origem')


idade = int(input('Qual sua idade? \n'))

if idade <= 12 and idade >= 0:
    print('Criança: 0 a 12 anos')
elif idade >= 13 and idade <= 18:
    print('Adolescente: 13 a 18 anos')   
else:
    print('Adulto: acima de 18 anos')


usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")
