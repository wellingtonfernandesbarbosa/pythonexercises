def aumentar(preco, taxa, formatar=False):
    '''
    -> Função para
    :param preco:
    :param taxa:
    :param formatar:
    :return:
    '''
    res = preco + (preco * taxa / 100)
    return res if formatar is False else moeda(res)


def diminuir(preco, desconto, formatar=False):
    res = preco - (preco * desconto / 100)
    return res if not formatar else moeda(res)


def dobro(preco, formatar=False):
    res = preco * 2
    if formatar:
        return moeda(res)
    return res


def metade(preco, formatar=False):
    res = preco / 2
    if formatar:
        return moeda(res)
    return res


# noinspection NonAsciiCharacters
def moeda(preço=0, tipo='R$'):
    return f'{tipo} {preço:.2f}'.replace('.', ',')


def resumo(preco, taxa=0, desconto=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{desconto}% de deconto: \t{diminuir(preco, desconto, True)}')
    print('-' * 30)
