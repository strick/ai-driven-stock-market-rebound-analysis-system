from dotenv import load_dotenv
import requests
import os
import sys
import json

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from config import RAW_DATA_DIR

RAW_DATA_DIR = project_root + RAW_DATA_DIR

load_dotenv()

def fetch_stock_data(stock_symbol):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    daily_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}'
    monthly_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock_symbol}&apikey={api_key}'

    # Fetching data
    r_daily = requests.get(daily_url)
    r_monthly = requests.get(monthly_url)
    data = {'daily': r_daily.json(), 'monthly': r_monthly.json()}

    # Define file paths
    daily_file_path = os.path.join(RAW_DATA_DIR, f"{stock_symbol}_daily.json")
    monthly_file_path = os.path.join(RAW_DATA_DIR, f"{stock_symbol}_monthly.json")

    # Write data to files
    with open(daily_file_path, 'w') as file:
        json.dump(data['daily'], file)
    
    with open(monthly_file_path, 'w') as file:
        json.dump(data['monthly'], file)

    return data

fetch_stock_data('IFRX')