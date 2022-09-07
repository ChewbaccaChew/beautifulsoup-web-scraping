import requests
import fake_useragent
from bs4 import BeautifulSoup

LINK = "https://zastavok.net/"
image_number = 0
storage_number = 1

for storage in range(2):

    response = requests.get(f"{LINK}/{storage_number}").text
    soup = BeautifulSoup(response, "lxml")
    block = soup.find("div", class_="block-photo")
    all_image = block.findAll("div", class_="short_full")

    for image in all_image:
        image_link = image.find("a").get("href")
        download_storage = requests.get(f"{LINK}/{image_link}").text
        download_soup = BeautifulSoup(download_storage, "lxml")
        download_block = download_soup.find("div", class_="image_data").find("div", class_="block_down")
        result_link = download_block.find("a").get("href")

        # Download image
        image_bytes = requests.get(f"{LINK}/{result_link}").content

        with open(f"image/{image_number}.jpg", "wb") as file:
            file.write(image_bytes)

        image_number += 1
        print(f"Изображение {image_number}.jpg успешно скачано!")

    storage_number += 1
