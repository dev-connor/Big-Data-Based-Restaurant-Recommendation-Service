from bs4 import BeautifulSoup
import requests

url = 'https://www.musinsa.com/app/contents/onsale'
params = {
    'd_cat_cd': '018',
    'page_kind': 'onsale',
    'list_kind': 'small',
    'sort': 'pop_category',
    'page': '1',
    'display_cnt': '90',
    'sale_fr_rate': '70',
    'sale_yn': 'Y',
    'sale_dt_yn': 'Y',
    'sale_campaign_ym': 'N',
    'chk_timesale': 'on',
}

response = requests.get(url,params=params)
print(response.status_code)