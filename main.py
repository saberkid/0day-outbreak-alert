
import requests
from bs4 import BeautifulSoup
import datetime

ODAY_BASE_URL = "https://0day.today"

# headers = {
#     'authority': '0day.today',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'sec-fetch-dest': 'document',
#     'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'referer': 'https://0day.today/exploit/description/37197',
#     'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
#     'cookie': '__utmz=200109231.1642193513.1.1.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/; PHPSESSID=34cb4f67d8ae563aafeff17fc417ec6e; __utmc=200109231; __utma=200109231.104222644.1642193513.1642463939.1642537823.4; __utmt=1; __utmb=200109231.5.10.1642537823; popup=off',
# }
headers = {
    'authority': '0day.today',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://0day.today/',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'cookie': '__utmz=200109231.1642193513.1.1.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/; PHPSESSID=34cb4f67d8ae563aafeff17fc417ec6e; __utmc=200109231; popup=off; __utma=200109231.104222644.1642193513.1642545660.1642549024.6; __utmt=1; hash=3c71cb1d249ab4eacced8437b558a9d6; __utmb=200109231.9.10.1642549024',
}
response = requests.get('https://0day.today/remote/1', headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
for row in soup.find_all('div', class_="ExploitTableContent"):
  table_content = row.find_all('a')
  publish_date = datetime.datetime.strptime(table_content[0].text, "%d-%m-%Y")
  title = table_content[1].text

  now = datetime.datetime.now() # current date and time
  last_month = now - datetime.timedelta(days=30)
  if publish_date > last_month:
    description_url = ODAY_BASE_URL + table_content[1].get('href')

    print(title + ' ' + description_url)

# response = requests.get('https://0day.today/exploit/description/37197', headers=headers)
