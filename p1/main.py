import os
from dotenv import load_dotenv
import csv
import requests

load_dotenv() 

# constants
BASE_URL = 'https://finnhub.io/api/v1' 
TICKERS = ('AAPL', 'AMZN', 'NFLX', 'META', 'GOOGL')
API_KEY = os.getenv('API_KEY')
CSV_FILE_NAME = 'output.csv'
ROW_NAMES = ('stock_symbol', 'percentage_change', 'current_price', 'last_close_price')

def main():
    #save this to CSV file 
    most_volatile_stock = ['', 0.0000, 0.00, 0.00] # [ticker, percentage_change, current_price, last_close_price]

    with requests.session() as session:
        for ticker in TICKERS:
            response = session.get(f'{BASE_URL}/quote?token={API_KEY}&symbol={ticker}')
            
            # https://finnhub.io/docs/api/quote
            data = response.json()

            # check data output
            print(ticker, data)
            
            # if percentage point is greater than current, replace
            if data['dp'] > most_volatile_stock[1]:
                most_volatile_stock = [ticker, data['dp'], data['c'], data['pc']]
            
    print('Most Volatile Stock', most_volatile_stock)

    # create/overwrite output.csv file
    with open(CSV_FILE_NAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(ROW_NAMES)
        writer.writerow(most_volatile_stock)


if __name__ == '__main__':
    main()



