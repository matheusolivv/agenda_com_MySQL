import mysql.connector
from exibir_contatos import ver_todos


uuser = 'epiz_22941340'
ppassowrd = 'xxx'
hhost = 'sql100.epizy.com'
ddatabase = 'epiz_22941340_meu_banco'


def remover():
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()

    while True:
        print('PAINEL DE REMOÇÃO DE CONTATOS, USE COM CUIDADO')
        input('ENTER para continuar')

        while True:
            try:
                print('''
    
                    ---------AGENDA-------------

                    REMOVER CONTATO         [ 1 ]
                    SAIR                    [ 2 ]

                    -----------------------------    
                                                ''')
                opcao = int(input('Escolha apenas uma das OPCOES ACIMA: '))
                if opcao > 2 or opcao < 1:
                    opcao = int(input('Escolha 1 ou 2: '))
                else:
                    break
            except:
                print('Ops... APENAS NÚMEROS, tente novamente! ')
        if opcao == 2:
            break

        while True:
            ver_todos()
            try:
                id = ''
                if len(str(id)) < 1:
                    id = int(input('Digite um ID PARA DELETAR o contato: '))

            except:
                print('Ops... Este campo não pode ficar vazio \n')


            else:
                if len(str(id)) > 1:
                    id = str(id)
                    id = f'{id}'
                    cursor.execute(f'delete from agenda.contatos where id = "{id}"')
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    break


