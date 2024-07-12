#Perguntas, respostas e resposta correta formuladas em dicionários.
questoes = [
    {
        'Pergunta': 'O que é inflação?',
        'Opções': ['Aumento geral dos preços, reduzindo o poder de compra do dinheiro.',
                   'Redução geral dos preços, aumentando o poder de compra do dinheiro.',
                   'Estagnação dos preços, mantendo o poder de compra do dinheiro.',
                   'Taxa de juros cobrada pelos bancos.'],
        'Resposta': 'Aumento geral dos preços, reduzindo o poder de compra do dinheiro.',
    },
    {
        'Pergunta': 'O que é PIB?',
        'Opções': ['Soma de todos os salários pagos em um país em um ano.',
                   'Soma de todos os bens e serviços finais produzidos em um país em um ano.',
                   'Taxa de desemprego em um país em um ano.',
                   'Número de empresas em operação em um país em um ano.'],
        'Resposta': 'Soma de todos os bens e serviços finais produzidos em um país em um ano.',
    },
    {
        'Pergunta': 'O que são taxas de juros?',
        'Opções': ['Custo do dinheiro emprestado, expresso como uma porcentagem.',
                   'Aumento geral dos preços de bens e serviços.',
                   'Valor total das exportações de um país.',
                   'Quantidade de dinheiro em circulação.'],
        'Resposta': 'Custo do dinheiro emprestado, expresso como uma porcentagem.',
    },
    {
        'Pergunta': 'O que é política monetária?',
        'Opções': ['Medidas do governo para reduzir o desemprego.',
                   'Políticas para aumentar a produção agrícola.',
                   'Estratégias para reduzir a inflação aumentando os impostos.',
                   'Ações do banco central para controlar a oferta de dinheiro e as taxas de juros.'],
        'Resposta': 'Ações do banco central para controlar a oferta de dinheiro e as taxas de juros.',
    },
    {
        'Pergunta': 'O que é oferta e demanda?',
        'Opções': ['A taxa de crescimento do PIB de um país.',
                   'O número total de empresas em um mercado.',
                   'O princípio econômico que descreve a quantidade de um bem ou serviço disponível e a vontade dos consumidores de comprá-lo.',
                   'A quantidade de dinheiro que o governo imprime.'],
        'Resposta': 'O princípio econômico que descreve a quantidade de um bem ou serviço disponível e a vontade dos consumidores de comprá-lo.',
    },
    {
        'Pergunta': 'O que é política fiscal?',
        'Opções': ['Conjunto de medidas do governo para controlar a oferta de dinheiro e as taxas de juros.',
                   'Ações do banco central para regular a quantidade de dinheiro na economia.',
                   'Decisões sobre impostos, gastos e endividamento público para alcançar objetivos econômicos.',
                   'O conjunto de leis que regulam o comércio internacional.'],
        'Resposta': 'Decisões sobre impostos, gastos e endividamento público para alcançar objetivos econômicos.',
    },
]

#Contagem de acertos a partir de zero
quantidade_acertos = 0

for pergunta in questoes: 
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes, start=1):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção (digite o número da opção): ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha) - 1

    if escolha_int is not None:
        if 0 <= escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        quantidade_acertos += 1
        print(f'Você Acertou! 😁\n{35*'-'}')
    else:
        print(f'Você Errou. 😔\n{35*'-'}'),

print(f'{35*'-'}\n|  Você acertou {quantidade_acertos} de {len(questoes)} perguntas. |\n{35*'-'}')