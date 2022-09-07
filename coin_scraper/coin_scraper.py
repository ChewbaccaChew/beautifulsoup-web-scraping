import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

USER = UserAgent().random
HEADERS = {"user-agent": USER}
LINK = "https://coinmarketcap.com/"

while True:
    response = requests.get(LINK, headers=HEADERS).text
    soup = BeautifulSoup(response, "lxml")

    blocks = soup.find("tbody").find_all("tr")

    for coin in blocks:
        coin_name = coin.find(class_="cmc-link")

        if "bitcoin" in coin_name.get("href"):
            price_block = coin.find(class_="sc-131di3y-0")
            coin_price = price_block.find("a").text

            result = f"BITCOIN: {coin_price}"
            print(result, end='')
            time.sleep(3)
            print('\b' * len(result), end='', flush=True)
            break

    time.sleep(1)
