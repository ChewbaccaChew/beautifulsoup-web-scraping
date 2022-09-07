import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

USER = UserAgent().random
HEADER = {'user-agent': USER}
LINK = "https://browser-info.ru/"

response = requests.get(LINK, headers=HEADER).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id="tool_padding")

# with open("1.html", "w", encoding="utf-8") as file:
#     file.write(response)

# check JS
check_js = block.find('div', id="javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'JavaScript: {status_js}'

# check Fl
check_fl = block.find('div', id="flash_version")
status_fl = check_fl.find_all('span')[1].text
result_fl = f'Flash: {status_fl}'

# check UA
check_ua = block.find('div', id="user_agent").text

print(result_js)
print(result_fl)
print(check_ua)
