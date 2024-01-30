from flask import Flask, render_template, request
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

#@app.route('/')
#def home():
#    data = get_stock_data('IFRX')  # Call get_stock_data with the desired symbol
#    return json.dumps(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis = None
    if request.method == 'POST':
        stock_ticker = request.form['stock_ticker']
        # Placeholder for AI Model Analysis
        analysis = get_analysis(stock_ticker)
        # Placeholder for GenAI Interaction
        genai_response = get_genai_response(stock_ticker)
        return render_template('index.html', analysis=analysis, genai_response=genai_response)
    return render_template('index.html', analysis=analysis)

def get_analysis(stock_ticker):
    # Placeholder function for AI model analysis
    # Replace with actual analysis logic
    return f"Analysis for {stock_ticker}"

def get_genai_response(stock_ticker):
    # Placeholder function for GenAI interaction
    # Replace with actual GenAI interaction logic
    return f"GenAI response for {stock_ticker}"

if __name__ == '__main__':
    app.run(debug=True)
