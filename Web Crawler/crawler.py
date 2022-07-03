import requests
import io
from bs4 import BeautifulSoup


def get_http(url, nome_livro):
    nome_livro = nome_livro.replace(' ', '%20')
    url = '{0}s/{1}'.format(url, nome_livro)

    try:
        return requests.get(url)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
            requests.excepetions.ConnectionError, requests.exceptions.Timeout) as e:
        print(str(e))
        pass
    except Exception as e:
        raise


def get_produtos(content):
    soup = BeautifulSoup(content, 'lxml')
    produtos = soup.find_all('div', {'class': 'resItemBox resItemBoxBooks exactMatch'})

    lista_produtos = []
    for produto in produtos:
        info_produto = (produto.find('h3', {'itemprop': 'name'})).a.string
        info_produto += '\nIdioma: '
        if produto.find('div', {'class': 'bookProperty property_language'}) is not None:
            info_produto += (produto.find('div', {'class': 'bookProperty property_language'})).find('div', {
                'class': 'property_value'}).string
        else:
            info_produto += 'Não informado'
        info_produto += '\nArquivo: ' + (produto.find('div', {'class': 'bookProperty property__file'})).find('div', {
            'class': 'property_value'}).string
        info_produto += ' {' + 'https://b-ok.lat' + produto.a.get('href') + '}'
        lista_produtos.append(info_produto)
    return lista_produtos


if __name__ == '__main__':

    nome_livro = input("Busque por um livro ou palavras-chave: ")

    url = 'https://b-ok.lat/'

    r = get_http(url, nome_livro)

    if r:
        lista_produtos = get_produtos(r.text)

    with io.open('lista de livros.txt', 'w', encoding='utf-8') as f:
        f.write('Resultados encontrados para \'' + nome_livro + '\':')
        for i in range((int(len(lista_produtos)))):
            f.write('\n\n' + str(lista_produtos[i]))

    with io.open('lista de livros.txt', 'r', encoding='utf-8') as f:
        print('\n' + f.read())
