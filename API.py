from pprint import pprint
import yfinance as yf
data = yf.download("SPY AAPL", start="2019-04-01", end="2019-04-30")
print(data)
