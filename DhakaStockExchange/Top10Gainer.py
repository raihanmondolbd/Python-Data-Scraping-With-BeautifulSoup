# import requests
# from bs4 import BeautifulSoup
# import openpyxl
#
#
# # source = requests.get('https://www.dsebd.org/top_ten_gainer.php')
# source = requests.get('https://www.dsebd.org/')
#
# soup = BeautifulSoup(source.text, 'html.parser')
# # print(soup)
# table_heading = soup.find('.table>tbody')
# # table_row = table_heading[0].parent.parent.parent
# print(table_heading)


from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated Tv Shows"
sheet.append(['Rank', 'Tv Shows Name', 'Release Year', 'IMDB Rating'])

try:
    source = requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
    # if url does not exist then raise error
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    for movie in movies:
        name = movie.find('td', class_="titleColumn").a.text
        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split(".")[0]
        year = movie.find('td', class_="titleColumn").span.text.strip("()")
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating])

except Exception as e:
    print(e)

excel.save("../IMDB/IMDB Tv Shows Rating.xlsx")






