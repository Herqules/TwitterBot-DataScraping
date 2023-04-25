import requests
import json
from prettytable import PrettyTable

# Replace YOUR_API_KEY with your actual Alpha Vantage API key
API_KEY = "API KEY HERE"

def get_stock_info(stock_symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)

    # Retrieve relevant information from the API response
    symbol = data["Global Quote"]["01. symbol"]
    price = data["Global Quote"]["05. price"]
    change_percent = data["Global Quote"]["10. change percent"]
    volume = data["Global Quote"]["06. volume"]
    latest_trading_day = data["Global Quote"]["07. latest trading day"]

    # Print stock information in a pretty table
    table = PrettyTable()
    table.field_names = ["Stock Symbol", "Price", "Change Percent", "Volume", "Latest Trading Day"]
    table.add_row([symbol, price, change_percent, volume, latest_trading_day])
    print(table)

# Prompt user for stock symbol input
stock_symbol = input("Enter the stock symbol: ")

# Get and display stock information
get_stock_info(stock_symbol.upper())
