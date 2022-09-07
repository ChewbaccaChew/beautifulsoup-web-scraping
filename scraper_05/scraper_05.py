# https://www.tury.ru/hotel/most_luxe.php

import requests
from bs4 import BeautifulSoup


def get_req():

    for i in range(0, 90, 30):
        URL = f"https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&s={i}"
        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }

        req = requests.get(url=URL, headers=HEADERS)

        with open("index.html", "a", encoding="utf-8") as file:
            file.write(req.text)


def go_bs4():

    with open("index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    hotels_cards = soup.find_all("div", class_="hotel_card_dv")

    count = 0
    for card in hotels_cards:
        print(f'{card.find("a").get("href")}')
        count += 1

    print(count)


def main():
    # get_req()
    go_bs4()


if __name__ == "__main__":
    main()
