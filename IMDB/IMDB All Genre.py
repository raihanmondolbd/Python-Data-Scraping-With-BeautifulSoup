import requests
from bs4 import BeautifulSoup
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Genre List"
sheet.append(["Genre Name", "Genre Link"])



source = requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
soup = BeautifulSoup(source.text, 'html.parser')

genres = soup.find("ul", class_='quicklinks').find_all("li")
for genre in genres:
    genre_name = genre.text.strip()
    genre_link = genre.find("a", href=True).get('href').strip(",")
    print(genre_name, genre_link)
    sheet.append([genre_name, genre_link])


excel.save('../Excel/IMDB/IMDB Genre List.xlsx')
