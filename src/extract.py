import requests
import logging
import os
from config import API_URL, API_KEY


def fetch_data(symbol="AAPL"):
    """
    Fetch data from the API for the given symbol.
    """
    try:
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": API_KEY
            
        }
        response = requests.get(API_URL, params=params)
        # print("hello")
        # print(response)
        response.raise_for_status()
        data = response.json()
        # print(data)
        if "Time Series (Daily)" in data:
            return data["Time Series (Daily)"]
        else:
            raise ValueError("API response does not contain 'Time Series (Daily)' data.")
    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        raise

# fetch_data()

