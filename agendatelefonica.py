# Trabalho de Computação 1
# Alunos: Gabriel Flores, Yuri Coutinho e Eduardo Ferreira
# Professor: Juliano Caldeira
# Descrição: agenda telefônica corporativa


# Função que define se o contato, o qual o usuário procura, existe. Caso exista, retorna True. Caso não, retorna False.

def ExisteContato(agenda, email):
    if len(agenda) > 0:
        for contato in agenda:
            if contato['E-mail'] == email:
                return True
    return False


# Após as modificações na lista agenda, está função replica a atualização no arquivo texto "contatos.txt" Será acionada nos caso de
# adicionar contato, editar contato e excluir contato.
# Optamos por usar o linha.split para manipular o arquivo texto de acordo com o separador ultilizado (#)

def SalvarContato(agenda):
    arquivo = open('contatos.txt', 'w')
    for contato in agenda:
        arquivo.write('{}#{}#{}#{}\n'.format(contato['Nome'], contato['Celular'], contato['Residencial'], contato['E-mail']))
    arquivo.close()


# Ao abrir novamente o programa, essa função garante que a agenda tenha acesso ao arquivo texto que estava sendo manipulado. Se essa função não existisse
# sempre que o usuário reiniciasse o programa, a agenda estaria zerada.

def CarregarContatos():
    agenda = []
    try:

        arquivo = open('contatos.txt', 'r')

        for linha in arquivo.readlines():
            coluna = linha.strip().split('#')

            contato = {'Nome': coluna[0], 'Celular': coluna[1], 'Residencial': coluna[2],
                       'E-mail': coluna[3]}

            agenda.append(contato)
        arquivo.close()
    except FileNotFoundError:
        pass
    return agenda


# Função que edita o contato. Pede ao usuário o email do contato, e caso encontrado, altera os parâmetros desejados.
# O len(agenda) que inicia a função garante que a agenda ja tenha pelo menos um usuário para que possa ser editado. Caso a agenda não tenha nenhum contato,
# o usuário não terá o que editar.
# A função também garante, através do ExisteContato que o usuário somente editará contatos existentes

def EditarContato(agenda):
    print('\n___________________________________\nEDITAR CONTATO\n\n')
    if len(agenda) > 0:
        email = input('Digite o Email do contato a ser alterado:  ')
        if ExisteContato(agenda, email):
            print('\nO contato foi encontrado. As informacoes seguem abaixo:  ')
            for contato in agenda:
                if contato['E-mail'] == email:
                    print('\tNome: {}'.format(contato['Nome']))
                    print('\tEmail: {}'.format(contato['E-mail']))
                    print('\tCelular: {}'.format(contato['Celular']))
                    print('\tResidencial: {}'.format(contato['Residencial']))
                    print()
                    print('\nRealize suas modificacoes: \n')
                    contato['Nome'] = input('\tDigite o novo nome do contato:  ')
                    contato['E-mail'] = input('\tDigite o novo email do contato:  ')
                    contato['Celular'] = input('\tDigite o novo numero de celular do contato:  ')
                    contato['Residencial'] = input('\tDigite o novo numero residencial do contato:  ')
                    print()
                    print('Os dados de {} foram alterados com sucesso.'.format(contato['Nome']))
                    break
        else:
            print('\n\tNao existe contato cadastrado no sistema com o email {}.'.format(email))
    else:
        print('\tNao existe nenhum contato cadastrado no sistema.')


# Função que exclui o contato. Pede ao usuário o email do contato, e caso encontrado, exclui-o.
# O len(agenda) que inicia a função garante que a agenda ja tenha pelo menos um usuário para que possa ser excluído. Caso a agenda não tenha nenhum contato,
# o usuário não terá o que excluir.
# A função também garante, através do ExisteContato que o usuário somente excluirá contatos existentes.

def ExcluirContato(agenda):
    print('\n___________________________________\nEXCLUIR CONTATO\n\n')
    if len(agenda) > 0:
        email = input('Digite o Email do contato a ser excluido: ')
        if ExisteContato(agenda, email):
            print('\nO contato foi encontrado. As informacoes seguem abaixo: ')
            for i, contato in enumerate(agenda):
                if contato['E-mail'] == email:
                    print('\n\tNome: {}'.format(contato['Nome']))
                    print('\tEmail: {}'.format(contato['E-mail']))
                    print('\tCelular: {}'.format(contato['Celular']))
                    print('\tResidencial: {}'.format(contato['Residencial']))
                    print( )
                    del agenda[i]
                    print('\tO CONTATO FOI APAGADO COM SUCESSO!.')
                    break
        else:
            print('\n\tNao existe contato cadastrado no sistema com o email {}.'.format(email))
    else:
        print('\tNao existe nenhum contato cadastrado no sistema.')


# Função busca o contato especifico, caso este exista.
# O len(agenda) que inicia a função garante que a agenda ja tenha pelo menos um usuário para que possa ser buscado. Caso a agenda não tenha nenhum contato,
# o usuário não terá o que buscar.
# A função também garante, através do ExisteContato que o usuário somente buscará contatos existentes.

def BuscarContato(agenda):
    print('\n___________________________________\nBUSCAR CONTATO\n\n')
    if len(agenda) > 0:
        email = input('Digite o email do contato a ser encontrado no formato: ')
        if ExisteContato(agenda, email):
            print('\nO contato foi encontrado. As informacoes seguem abaixo:  ')
            for contato in agenda:
                if contato['E-mail'] == email:
                    print('\n\tNome: {}'.format(contato['Nome']))
                    print('\tEmail: {}'.format(contato['E-mail']))
                    print('\tCelular: {}'.format(contato['Celular']))
                    print('\tResidencial: {}'.format(contato['Residencial']))
        else:
            print('\n\tNao existe contato cadastrado no sistema com o email {}.'.format(email))
    else:
        print('\tNao existe nenhum contato cadastrado no sistema.')


# Função que adiciona contatos à agenda. O while True junto ao ExisteContato garante que o usuário não poderá adicionar contatos com o mesmo e-mail.

def AddContato(agenda):
    print('\n___________________________________\nADICIONAR CONTATO: \n\n')

    while True:
        email = input('\tE-mail: ')

        if not ExisteContato(agenda, email):
            break
        else:
            print('\nEsse email ja esta sendo utilizado.')
            print('Por favor, digite um novo email: \n')

    contato = {'Nome': input('\tNome: '), 'Celular': input('\tCelular: '), 'Residencial': input('\tResidencial: '),'E-mail': email}

    agenda.append(contato)
    print('\n\tO CONTATO {} FOI ADICIONADO COM SUCESSO'. format(contato['Nome']))


#Lista os contatos existentes, em forma de dicionario, na lista agenda.

def ListarContatos(agenda):
    print('\n___________________________________\nAGENDA TELEFÔNICA\n')
    if len(agenda) > 0:
        for i, contato in enumerate(agenda):
            print('\nContato {}'.format(i+1))
            print('\tNome: {}\n\tCelular: {}\n\tResidencial {}\n\tE-mail: {}'.format(contato['Nome'], contato['Celular'],
                contato['Residencial'], contato['E-mail']))
            print(' ')

        print('A agenda, atualmente, possui {} contato(s)'.format(len(agenda)))


    else:
        print('NÃO HÁ NENHUM CONTATO CADASTRADO NA AGENDA!')


def main():
    agenda = CarregarContatos()
    while True:
        op1 = str(input('\n___________________________________\n'
                         'AGENDA TELEFÔNICA: \n\n\tPressione [1] para adicionar um contato\n\tPressione [2] para editar um contato '  
                        '\n\tPressione [3] para excluir um contato\n\tPressione [4] para buscar os contatos\n\t'
                        'Pressione [5] para listar os contatos'
                        '\n\tPressione [6] para sair\n\nDigite sua opção: '))
        if op1 == '1':
            AddContato(agenda)
            SalvarContato(agenda)
        elif op1 == '2':
            EditarContato(agenda)
            SalvarContato(agenda)
        elif op1 == '3':
            ExcluirContato(agenda)
            SalvarContato(agenda)
        elif op1 == '4':
            BuscarContato(agenda)
        elif op1 == '5':
            ListarContatos(agenda)
        elif op1 == '6':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Porfavor, tente novamente!\n')


#Programa Principal


main()
