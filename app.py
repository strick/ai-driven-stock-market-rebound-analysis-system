from flask import Flask
import requests
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)
load_dotenv()

# This is just a regular function, not a route
def get_stock_data(stock_symbol):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data

@app.route('/')
def home():
    data = get_stock_data('IFRX')  # Call get_stock_data with the desired symbol
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)
