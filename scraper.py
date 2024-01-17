from bs4 import BeautifulSoup
import requests

url = 'https://www.musinsa.com/categories/item/018'
params = {
}
headers = {
    'user-agent': "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'"
}

response = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
list_box = soup.find('div', class_='list-box')
print(list_box)
