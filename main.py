# scraping carousel_id pada halaman listing
import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/u/carousell_id/'

contents = requests.get(url)
# print(contents.text)

response = bs4.BeautifulSoup(contents.text, 'html.parser')
# print(response)
data = response.find_all('div', 'D_lN D_ut M_mt D_uv M_mv')
print(data[0].text)



