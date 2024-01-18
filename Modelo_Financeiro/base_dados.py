import yfinance as yf
import yfinance as yf
import investpy as inv
import pandas as pd

vale = yf.Ticker("VALE3.SA")

print(vale.get_financials(freq='quarterly'))

