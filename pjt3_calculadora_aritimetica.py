while True:
    print(f'''{30*"-"}
Selecione a operação: 
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
{30*"-"}''')

    opcao = input('Opção: ')

    if opcao in ['1', '2', '3', '4']:
        digito1 = int(input('Digite o primeiro número: '))
        digito2 = int(input('Digite o segundo número: '))
        
        if opcao == '1':
            resultado = digito1 + digito2
            print(f'{digito1} + {digito2} = {resultado}')
        elif opcao == '2':
            resultado = digito1 - digito2
            print(f'{digito1} - {digito2} = {resultado}')
        elif opcao == '3':
            resultado = digito1 * digito2
            print(f'{digito1} * {digito2} = {resultado}')
        elif opcao == '4':
            if digito2 != 0:
                resultado = digito1 / digito2
                print(f'{digito1} / {digito2} = {resultado}')
            else:
                print('Não é possível divisão por zero.')
    else:
        print('OPÇÃO INVÁLIDA.')