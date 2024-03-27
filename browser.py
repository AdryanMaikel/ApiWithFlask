"""

"""

from requests import get
from bs4 import BeautifulSoup as soup

URL_GOOGLE_FINANCE = 'https://www.google.com/finance/quote/'


def get_price_cripto(tag: str) -> dict[str, str]:
    RESPONSE = get(f"{URL_GOOGLE_FINANCE}{tag}-BRL?hl=pt")
    SOUP = soup(RESPONSE.text, 'html.parser')
    price = SOUP.find(class_="YMlKec fxKbKc").text
    name = SOUP.find(class_="zzDege").text
    return {"name": name, "price": f"R$ {price}"}


if __name__ == "__main__":
    price = get_price_cripto('BTC')
    print(price)

    pass
