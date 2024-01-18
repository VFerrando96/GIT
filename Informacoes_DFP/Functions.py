import requests
import pandas as pd
import os
import zipfile

atual=os.getcwd()
os.chdir(f"{atual}/informacoes_DFP/Arquivos")

def Baixar_dados_abertos(ano):
    url='https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
    download= requests.get(url + f"dfp_cia_aberta_{ano}.zip")
    open(f"dfp_cia_aberta_{ano}.zip",'wb').write(download.content)

def Descompactar_arquivos_completo_zip():
    lista_demostracoes_2010_2022 = []
    pasta=f"{atual}/informacoes_DFP/Arquivos"
    for arquivo in os.listdir(os.chdir(pasta)):
       if os.path.getsize(os.path.join(pasta, arquivo)) >= 1024:
           arquivo_zip = zipfile.ZipFile(os.path.join(pasta, arquivo))
           for planilha in arquivo_zip.namelist():
                demonstracao = pd.read_csv(arquivo_zip.open(planilha), sep=';', encoding='ISO-8859-1', dtype={"ORDEM_EXERC": "category"})
                lista_demostracoes_2010_2022.append(demonstracao)
    base_dados = pd.concat(lista_demostracoes_2010_2022)
    base_dados[['con_ind','tipo_dem']] = base_dados['GRUPO_DFP'].str.split("-",expand=True)
    base_dados['con_ind']=base_dados['con_ind'].str.strip()
    base_dados['tipo_dem']=base_dados['tipo_dem'].str.strip()
    base_dados = base_dados[base_dados['ORDEM_EXERC'] != 'PENÚLTIMO']
    base_dados.to_csv(f"{atual}/informacoes_DFP/Base/Base_dados_completa.csv",sep=';')

def Descompactar_arquivo_ano(ano):
    demonstracao_ano=[]
    pasta = f"{atual}/informacoes_DFP/Arquivos"
    arquivo=f"{atual}/informacoes_DFP/Arquivos/"+ f"dfp_cia_aberta_{ano}.zip"
    if os.path.exists(arquivo):
        arquivo_zip = zipfile.ZipFile(os.path.join(pasta, arquivo))
        for planilha in arquivo_zip.namelist():
            demonstracao = pd.read_csv(arquivo_zip.open(planilha), sep=';', encoding='ISO-8859-1', dtype={"ORDEM_EXERC": "category"})
            demonstracao_ano.append(demonstracao)
            base_dados = pd.concat(demonstracao_ano)
        base_dados[['con_ind','tipo_dem']] = base_dados['GRUPO_DFP'].str.split("-",expand=True)
        base_dados['con_ind']=base_dados['con_ind'].str.strip()
        base_dados['tipo_dem']=base_dados['tipo_dem'].str.strip()
        base_dados = base_dados[base_dados['ORDEM_EXERC'] != 'PENÚLTIMO']
        base_dados.to_csv(f"{atual}/informacoes_DFP/Base/Base_dados_{ano}.csv",sep=';')
    else:
        print("Não existe arquivo para essa data")

def Descompactar_DRE_ano(ano,cnpj):
    demonstracao_ano=[]
    pasta = f"{atual}/informacoes_DFP/Arquivos"
    arquivo=f"{atual}/informacoes_DFP/Arquivos/"+ f"dfp_cia_aberta_{ano}.zip"
    if os.path.exists(arquivo):
        arquivo_zip = zipfile.ZipFile(os.path.join(pasta, arquivo))
        for planilha in arquivo_zip.namelist():
            demonstracao = pd.read_csv(arquivo_zip.open(planilha), sep=';', encoding='ISO-8859-1', dtype={"ORDEM_EXERC": "category"})
            demonstracao_ano.append(demonstracao)
            base_dados = pd.concat(demonstracao_ano)
        base_dados[['con_ind','tipo_dem']] = base_dados['GRUPO_DFP'].str.split("-",expand=True)
        base_dados['con_ind']=base_dados['con_ind'].str.strip()
        base_dados['tipo_dem']=base_dados['tipo_dem'].str.strip()
        base_dados = base_dados[base_dados['ORDEM_EXERC'] != 'PENÚLTIMO']
        base_dados=base_dados[base_dados['CNPJ_CIA'] == f'{cnpj}']
        base_dados.to_csv(f"{atual}/informacoes_DFP/Base/DRE_{ano}.csv",sep=';')
    else:
        print("Não existe arquivo para essa data")