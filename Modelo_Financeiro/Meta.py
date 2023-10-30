from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from io import StringIO
import MetaTrader5 as mt5
driver = webdriver.Chrome()

driver.get('https://www.fundamentus.com.br/resultado.php')
local_tabela = '/html/body/div[1]/div[2]/table'
tabela = driver.find_element('xpath', local_tabela)
html_tabela = tabela.get_attribute('outerHTML')
tabela = pd.read_html(StringIO(html_tabela), thousands='.', decimal=',')[0]
tabela = tabela.set_index('Papel')
tabela = tabela[['Cotação', 'EV/EBIT', 'ROIC', 'Liq.2meses']]
tabela['ROIC'] = tabela['ROIC'].str.replace("%", "")
tabela['ROIC'] = tabela['ROIC'].str.replace(".", "")
tabela['ROIC'] = tabela['ROIC'].str.replace(",", ".")
tabela['ROIC'] = tabela['ROIC'].astype(float)
tabela = tabela[tabela['Liq.2meses'] > 1000000]
tabela = tabela[tabela['EV/EBIT'] > 0]
tabela = tabela[tabela['ROIC'] > 0]
tabela['ranking_ev_ebit'] = tabela['EV/EBIT'].rank(ascending = True)
tabela['ranking_roic'] = tabela['ROIC'].rank(ascending = False)
tabela['ranking_final'] = tabela['ranking_ev_ebit'] + tabela['ranking_roic']
tabela = tabela.sort_values('ranking_final')
tabela=tabela.head(10)
tickers=tabela.index
#tickers_com_f = [ticker + 'F' for ticker in tickers]
print(tickers)
#######################################################################################################################################################################################
#   Iniciando o Meta Trader 5                                                                                                                                                         #  
#######################################################################################################################################################################################
# mt5.initialize(login=53477444, server="XPMT5-DEMO",password="899513Vi!")
# # shut down connection to the MetaTrader 5 terminal

# for acao in tickers:
#     mt5.symbol_select(acao)
#     preco=mt5.symbol_info(acao).ask
#     quantidade=1.0
#     ordem_compra = {
#             "action": mt5.TRADE_ACTION_DEAL,
#             "symbol": acao,
#             "volume": quantidade,
#             "type": mt5.ORDER_TYPE_BUY,
#             "price": preco,
#             "magic": 1,
#             "comment": "Trades hackeando a bolsa",
#             "type_time": mt5.ORDER_TIME_DAY,
#             "type_filling": mt5.ORDER_FILLING_RETURN,
#     }
#     compra = mt5.order_send(ordem_compra)
#     print(compra)
