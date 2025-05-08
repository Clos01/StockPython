import yfinance as yf
import backtrader as bt
from polygon import RESTClient
from dotenv import load_dotenv, find_dotenv
import os

# Locate and load the .env file
load_dotenv(find_dotenv())

# Access the API key from environment variables
polygon_api_key = os.getenv("POLYGON_API_KEY")

client = RESTClient(api_key=polygon_api_key)

