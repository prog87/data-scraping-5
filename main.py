# scraping carousel_id pada halaman listing
import bs4
import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/categories/6/?')
soup = BeautifulSoup(html_doc.text, 'html.parser')

kamera_terpopuler = soup.find(attrs={'class':'D_aH asm-browse-listings'})
# print(kamera_terpopuler)

titles = kamera_terpopuler.findAll(attrs={'class': 'D_Xc M_No D_Xe M_Np'})

for title in titles:
    # print(title)
    print(title.find('p',attrs={'class':'D_qE M_lC D_pQ M_lp D_qF M_lE D_qJ M_lI D_qM M_lL D_qP M_lO D_qR M_lQ D_qN M_lM D_qV'}))

# Scrapping tidak selesai karena situs menggunakan beberapa konten dinamis oleh JS
# solusi akan menggunakan selenium



