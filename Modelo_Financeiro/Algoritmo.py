#Formua mágica do Joel Grenblatt
import pandas as pd
import quantstats as qs

dados = pd.read_csv('Modelo_Financeiro/dados_empresas (1).csv')
dados=dados[dados['volume_negociado']>1000000]
valores_unicos = dados['ticker'].unique()
print(valores_unicos)