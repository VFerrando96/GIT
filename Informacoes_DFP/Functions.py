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

def Descompactar_arquivos_zip():
    lista_demostracoes_2010_2022 = []
    pasta=f"{atual}/informacoes_DFP/Arquivos"
    for arquivo in os.listdir(os.chdir(pasta)):
       if os.path.getsize(os.path.join(pasta, arquivo)) >= 1024:
           arquivo_zip = zipfile.ZipFile(os.path.join(pasta, arquivo))
           for planilha in arquivo_zip.namelist():
                demonstracao = pd.read_csv(arquivo_zip.open(planilha), sep=';', encoding='ISO-8859-1', dtype={"ORDEM_EXERC": "category"})
                lista_demostracoes_2010_2022.append(demonstracao)
    base_dados = pd.concat(lista_demostracoes_2010_2022)
    print(base_dados)
