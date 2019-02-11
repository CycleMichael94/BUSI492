import csv
import openpyxl
import pandas
import iexfinance
from iexfinance.stocks import Stock

#Unser inputs tickers and they are split
tinput = input('Enter the stock ticker: ')
tickers = tinput.split(' ')

#Output is defined and API request for stock data is made
company = Stock(tickers, output_format='pandas')

#API request is made for specific endpoints
info = company.get_company()
quote = company.get_quote()
keystat = company.get_key_stats()
#news = company.get_news()
#dfnews = pandas.DataFrame(news)
peers = company.get_peers()
dfpeers = pandas.DataFrame(peers)
dividends = company.get_dividends()
financials = company.get_financials()
chart = company.get_chart()



#Stock data is written into a single excel workbook
with pandas.ExcelWriter('new.xlsx') as writer:
    info.to_excel(writer, sheet_name='Info')
    quote.to_excel(writer, sheet_name='Quote')
    keystat.to_excel(writer, sheet_name='Key Stats')
    #dfnews.to_excel(writer, sheet_name='News', index=False)
    dfpeers.to_excel(writer, sheet_name='Peers', index=False)
    dividends.to_excel(writer, sheet_name='Dividends')
    chart.to_excel(writer, sheet_name='Chart')
