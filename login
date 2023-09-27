lista_email_cadastrado = []
lista_senha_cadastrado = []

email_novo_usuario = input('Digite o email do usuário: ')
senha_novo_usuario = input('Digite a senha do usuário: ')

if email_novo_usuario and senha_novo_usuario:

   if len(senha_novo_usuario) <= 13 :

      lista_email_cadastrado.append(email_novo_usuario)
      lista_senha_cadastrado.append(senha_novo_usuario)

   else:

      print(f'A senha digitada excede o limite de carcteres reservado para este campo')

else:

   print('Para cadastrar um usuário todos os campos devem estar preechidos podem f')
