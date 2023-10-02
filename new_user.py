nome = input('Digite o seu nome: ')
email = input('Digite o seu Email: ')
senha = input('Digite a sua Senha: ')

# escrevendo os dados em um arquivo txt

with open('dados.txt', 'w') as credenciais: # 
        credenciais.write(nome + '\n')
        credenciais.write(email + '\n')
        credenciais.write(senha + '\n')

# verificação do código do email


# se a verificação for bem sucedida

with open('dados.txt', 'r') as credenciais:
        nome_usuario = credenciais.readline()
        email_usuario = credenciais.readline()
        senha_usuario = credenciais.readline()

print(nome_usuario, )
