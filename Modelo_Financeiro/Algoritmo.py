#Formua mágica do Joel Grenblatt
import pandas as pd
import quantstats as qs
import matplotlib.pyplot as plt
dados = pd.read_csv('Modelo_Financeiro/dados_empresas (1).csv')
dados=dados[dados['volume_negociado']>1000000]
# print(dados)
#####################################################################   
#                       Calculo Retorno Mensal                      #
#####################################################################  
dados['retorno'] = dados.groupby('ticker')['preco_fechamento_ajustado'].pct_change()
dados['retorno']= dados['retorno'].shift(-1)

#####################################################################   
#                       Ranking EBIT e ROIC                           
#####################################################################  

dados['rankin_ebit'] = dados['retorno'] = dados.groupby('data')['ebit_ev'].rank(ascending=False)
dados['rankin_roic'] = dados['retorno'] = dados.groupby('data')['roic'].rank(ascending=False)

#####################################################################   
#                       soma dos ranks                          
#####################################################################  
dados['ranking_final'] = dados['rankin_ebit'] + dados['rankin_roic']

dados['ranking_final'] = dados.groupby('data')['ranking_final'].rank()

#####################################################################   
#                       Criando as carteiras                          
#####################################################################  
dados=dados[dados['ranking_final']<=10]

#####################################################################   
#                       rentabildiade por carteiras                          
##################################################################### 
rentabilidade_por_carteira=dados.groupby('data')['retorno'].mean()
rentabilidade_por_carteira = rentabilidade_por_carteira.to_frame()
#####################################################################   
#                       rentabildiade do modelo                        
##################################################################### 
rentabilidade_por_carteira['modelo'] = (1 + rentabilidade_por_carteira['retorno']).cumprod() - 1 

rentabilidade_por_carteiras = rentabilidade_por_carteira.shift(1)
rentabilidade_por_carteiras = rentabilidade_por_carteiras.dropna()

print(rentabilidade_por_carteiras)
#####################################################################   
#                       retorno ibov                       
##################################################################### 
ibov = pd.read_csv('Modelo_Financeiro/ibov (1).csv')

retornos_ibov = ibov['fechamento'].pct_change().dropna()
retornos_ibov_acum = (1 + retornos_ibov).cumprod() - 1 
rentabilidade_por_carteiras['ibovespa'] = retornos_ibov_acum.values


#####################################################################   
#                       grafico                       
##################################################################### 
qs.extend_pandas()

rentabilidade_por_carteiras.index = pd.to_datetime(rentabilidade_por_carteiras.index)
rentabilidade_por_carteiras['modelo'].plot_monthly_heatmap()
plt.show()