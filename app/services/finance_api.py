import requests
from app.config import Config

ALPHA_VANTAGE_API_KEY = Config.ALPHA_VANTAGE_API_KEY

def get_stock_price(symbol):
    """Fetches real-time stock price"""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return f"The stock price of {symbol} is ${data.get('Global Quote', {}).get('05. price', 'N/A')}"
