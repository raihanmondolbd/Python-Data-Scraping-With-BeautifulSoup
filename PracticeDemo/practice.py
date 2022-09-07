import openpyxl
import datetime

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "DSE Latest Price"
sheet.append(['Rank', 'Trading Code'])

dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
excelFileName = f'Practice Excel_{dateTime}'

sheet.append(['1', 'Trading Code'])

excel.save(f'../PracticeDemo/Excel/{excelFileName}.xlsx')
