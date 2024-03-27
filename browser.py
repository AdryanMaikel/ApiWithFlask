"""
    Arquivo encarregador de fazer requisições e lidar com HTML.
"""

from requests import get
from bs4 import BeautifulSoup as soup


def get_price_cripto(cripto: str) -> dict[str, str]:
    """Função usada para pegar o preço de uma criptomoeda passada por
    parametro ex:
    >>> get_price_cripto('BTC')
    ... {"name": "Bitcoin (BTC / BRL)", "price": "300.000,00"}

    :param cripto: str - Nome resumido da criptomoeda a ser pesquisada.
    :return: dict[str, str] - Dicionário contendo o nome e o preço.
    """
    RESPONSE = get(f'https://www.google.com/finance/quote/{cripto}-BRL?hl=pt')
    SOUP = soup(RESPONSE.text, 'html.parser')
    price = SOUP.find(class_="YMlKec fxKbKc").text
    name = SOUP.find(class_="zzDege").text
    return {"name": name, "price": price}


if __name__ == "__main__":
    price = get_price_cripto('BTC')
    print(price)
