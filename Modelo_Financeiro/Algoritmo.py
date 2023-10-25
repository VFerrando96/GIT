#Formua mágica do Joel Grenblatt
import pandas as pd
import quantstats as qs
import matplotlib.pyplot as plt
import monthly_returns_heatmap as mrh
import seaborn as sns
dados = pd.read_csv('Modelo_Financeiro/dados_empresas (1) (1).csv')
dados=dados[dados['volume_negociado']>1000000]

#####################################################################   
#                       Calculo Retorno Mensal                      #
#####################################################################  
dados['retorno'] = dados.groupby('ticker')['preco_fechamento_ajustado'].pct_change()
dados['retorno'] = dados.groupby('ticker')['retorno'].shift(-1)

# #####################################################################   
# #                       Ranking EBIT e ROIC                           
# #####################################################################  

dados['ranking_ebit_ev'] = dados.groupby('data')['ebit_ev'].rank(ascending = False)
dados['ranking_roic'] = dados.groupby('data')['roic'].rank(ascending = False)


# #####################################################################   
# #                       soma dos ranks                          
# #####################################################################  
dados['ranking_final'] = dados['ranking_ebit_ev'] + dados['ranking_roic']
dados['ranking_final'] = dados.groupby('data')['ranking_final'].rank()

# #####################################################################   
# #                       Criando as carteiras                          
# #####################################################################  
dados = dados[dados['ranking_final'] <= 10]


# #####################################################################   
# #                       rentabildiade por carteiras                          
# ##################################################################### 
rentabilidade_por_carteiras = dados.groupby('data')['retorno'].mean()
rentabilidade_por_carteiras = rentabilidade_por_carteiras.to_frame()

# #####################################################################   
# #                       rentabildiade do modelo                        
# ##################################################################### 
rentabilidade_por_carteiras['modelo'] = (1 + rentabilidade_por_carteiras['retorno']).cumprod() - 1 

rentabilidade_por_carteiras = rentabilidade_por_carteiras.shift(1)
rentabilidade_por_carteiras = rentabilidade_por_carteiras.dropna()

# #####################################################################   
# #                       retorno ibov                       
# ##################################################################### 
ibov = pd.read_csv('Modelo_Financeiro/ibov (1) (1).csv')

retornos_ibov = ibov['fechamento'].pct_change().dropna()
retornos_ibov_acum = (1 + retornos_ibov).cumprod() - 1 
rentabilidade_por_carteiras['ibovespa'] = retornos_ibov_acum.values
rentabilidade_por_carteiras = rentabilidade_por_carteiras.drop('retorno', axis = 1)

print(rentabilidade_por_carteiras)
# #####################################################################   
# #                       grafico                       
# ##################################################################### 
qs.extend_pandas()
rentabilidade_por_carteiras.index = pd.to_datetime(rentabilidade_por_carteiras.index)
rentabilidade_por_carteiras['modelo'].plot_monthly_heatmap()
rentabilidade_por_carteiras['ibovespa'].plot_monthly_heatmap()