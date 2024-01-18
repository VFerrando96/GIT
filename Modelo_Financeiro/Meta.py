from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from io import StringIO
import MetaTrader5 as mt5
import pulp
driver = webdriver.Chrome()
soma=0.0

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
tabela=tabela.head(15)
tickers=tabela.index
tickers_com_f = [ticker + 'F' for ticker in tickers]
print(tickers_com_f)

# #######################################################################################################################################################################################
# #   Iniciando o Meta Trader 5                                                                                                                                                      #  
# #######################################################################################################################################################################################
mt5.initialize(login=53477444, server="XPMT5-DEMO",password="899513Vi!")
# shut down connection to the MetaTrader 5 terminal
#######################################################################################################################################################################################
#   valor mínimo a ser usado para a compra das ações                                                                                                                                                    #  
######################################################################################################################################################################################
valor_disponivel = 1000000
problema = pulp.LpProblem("Selecao_de_Acoes", pulp.LpMaximize)
compra_acoes = []
preco_acoes = []
for acao in tickers:
    print(acao)
    compra_acoes.append(pulp.LpVariable(f"Compra_{acao}", lowBound=1, upBound=None, cat=pulp.LpInteger))
    preco_acoes.append(mt5.symbol_info(acao).ask)
problema += pulp.lpSum(preco_acoes[i] * compra_acoes[i] for i in range(15))

# Restrição: gastar no máximo o valor disponível
problema += pulp.lpSum(preco_acoes[i] * compra_acoes[i] for i in range(15)) <= valor_disponivel

# Restrição: comprar pelo menos uma ação de cada ticker
for i in range(15):
    problema += compra_acoes[i] >= 1
valor_max_por_acao = valor_disponivel / 10  # Divida igualmente o valor disponível
for i in range(15):
    problema += preco_acoes[i] * compra_acoes[i] <= valor_max_por_acao

# Resolva o problema
problema.solve()

acoes_selecionadas = {}
for i, acao in enumerate(tickers):
    quantidade_comprada = compra_acoes[i].varValue
    if quantidade_comprada > 0:
        acoes_selecionadas[acao] = quantidade_comprada

# Mostrar os resultados
if pulp.LpStatus[problema.status] == "Optimal":
    valor_gasto = sum(compra_acoes[i].varValue * preco_acoes[i] for i in range(15))
    print(f"Valor máximo gasto em ações: ${valor_gasto}")
    print("Carteira otimizada:")
    for acao, quantidade in acoes_selecionadas.items():
        mt5.symbol_select(acao)
        preco = mt5.symbol_info(acao).ask
        ordem_compra = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": acao,
            "volume": 100.0*quantidade,
            "type": mt5.ORDER_TYPE_BUY,
            "price": preco,
            "magic": 1,
            "comment": "Trades hackeando a bolsa",
            "type_time": mt5.ORDER_TIME_DAY,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        compra = mt5.order_send(ordem_compra)

        if compra.retcode == mt5.TRADE_RETCODE_DONE:
            print(f"Compra bem-sucedida de {quantidade} ações de {acao} a ${preco} cada.")
        else:
            print(f"Erro ao comprar {quantidade} ações de {acao}. Código de retorno: {compra.retcode}, Mensagem: {compra.comment}")
else:
    print("Não foi possível encontrar uma solução viável.")
# #######################################################################################################################################################################################
# #   Comprar as ações                                                                                                                                                                  #  
# ######################################################################################################################################################################################
# # for acao, quantidade in acoes_selecionadas.items():
# #     mt5.symbol_select(acao)
# #     preco = mt5.symbol_info(acao).ask
# #     ordem_compra = {
# #         "action": mt5.TRADE_ACTION_DEAL,
# #         "symbol": acao,
# #         "volume": quantidade,
# #         "type": mt5.ORDER_TYPE_BUY,  # Defina o tipo de ordem como compra (buy)
# #         "price": preco,
# #         "magic": 1,
# #         "comment": "Trades hackeando a bolsa",
# #         "type_time": mt5.ORDER_TIME_DAY,
# #         "type_filling": mt5.ORDER_FILLING_RETURN,
# #     }
# #     compra = mt5.order_send(ordem_compra)
    
# #     if compra.retcode == mt5.TRADE_RETCODE_DONE:
# #         print(f"Compra bem-sucedida de {quantidade} ações de {acao} a ${preco} cada.")
# #     else:
# #         print(f"Erro ao comprar {quantidade} ações de {acao}. Código de retorno: {compra.retcode}, Mensagem: {compra.comment}")
