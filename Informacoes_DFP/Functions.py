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

