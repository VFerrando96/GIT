#Formua mágica do Joel Grenblatt
import pandas as pd
import quantstats as qs

dados = pd.read_csv('Modelo_Financeiro/dados_empresas (1).csv')
dados=dados[dados['volume_negociado']>1000000]
# print(dados)
#####################################################################   
#                       Calculo Retorno Mensal                      #
#####################################################################  
dados['retorno'] = dados.groupby('ticker')['preco_fechamento_ajustado'].pct_change()
dados['retorno']= dados['retorno'].shift(-1)
print(dados)

