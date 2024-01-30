from flask import Flask
import requests
import os
from dotenv import load_dotenv
import json  # Add this import

app = Flask(__name__)
load_dotenv()  # This is the important part

@app.route('/')

def get_stock_data(stock_symbol='IFRX'):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')  # Accessing the API key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data  # Add this line to return the data

def home():
    data = get_stock_data('IFRX')
    return json.dumps(data)  # Convert dict to JSON string


if __name__ == '__main__':
    app.run(debug=True)
    # Test

