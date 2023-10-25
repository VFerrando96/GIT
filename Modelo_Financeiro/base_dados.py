import yfinance as yf
import yfinance as yf
import investpy as inv

br= inv.stocks.get_stocks(country='brazil')

carteira=[]
for a in br['symbol']:
    if len(a) <= 5:
        carteira.append(a+'.SA')


dt= yf.download(carteira,start='2002-01-01',end='2022-01-01')['Adj Close']
print(dt)