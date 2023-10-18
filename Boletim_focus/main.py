import Functions as f 
import requests

resultado = f.abrir_site_e_buscar_data_publicacao()
dia_hoje=f.Dia_de_hoje()

if rf'Data de publicação: 16/10/2023'  not in resultado:
    print('Boletim Saiu hoje')
    url_pdf=r"https://www.bcb.gov.br/content/focus/focus/R20231013.pdf"
    response = requests.get(url_pdf)
    if response.status_code == 200:
        print()