import datetime

import requests
from bs4 import BeautifulSoup
import openpyxl


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "DSE Latest Price"
sheet.append(['Rank', 'Trading Code', 'LTP*', 'HIGH', 'LOW', 'CLOSEP', 'YCP*', 'CHANGE', 'TRADE', 'VALUE(mm)', 'VOLUME'])

dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
excelFileName = f'Dhaka Stock Exchange_{dateTime}'

try:
    source = requests.get('https://www.dse.com.bd/latest_share_price_scroll_l.php')
    soup = BeautifulSoup(source.text, 'html.parser')

    latest_price_row = soup.select(".table > tbody, tr")

    for lr in latest_price_row[413:-2]:

        list_data = lr.text.split()
        rank = list_data[0]
        trading_code = list_data[1]
        ltp = list_data[2]
        high = list_data[3]
        low = list_data[4]
        closep = list_data[5]
        ycp = list_data[6]
        change = list_data[7]
        trade = list_data[8]
        value = list_data[9]
        volume = list_data[10]

        print(rank, trading_code, ltp, high, low, closep, ycp, change, trade, value, volume)
        sheet.append([rank, trading_code, ltp, high, low, closep, ycp, change, trade, value, volume])

    excel.save(f'../DhakaStockExchange/Excel/{excelFileName}.xlsx')
except Exception as e:
    print(e)
    print("Please, Try again after some time.")


