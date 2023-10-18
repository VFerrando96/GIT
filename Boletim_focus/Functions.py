from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import requests
driver = webdriver.Chrome()

def abrir_site_e_buscar_data_publicacao():
    url = "https://www.bcb.gov.br/publicacoes/focus"
    driver.get(url)
    xpath = "/html/body/app-root/app-root/div/div/main/dynamic-comp/div/div[1]/bcb-publicacao/div/div[1]/div/div/div[2]/div[1]/div[1]"
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    xpath_pdf = "/html/body/app-root/app-root/div/div/main/dynamic-comp/div/div[1]/bcb-publicacao/div/div[1]/div/div/div[2]/div[1]/div[1]"
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_pdf)))
    return(element.text)


def Dia_de_hoje():
    hoje = datetime.date.today()
    dia_de_hoje = hoje.day
    mes_de_hoje = hoje.month
    ano_de_hoje = hoje.year
    return(rf'{dia_de_hoje:02}/{mes_de_hoje:02}/{ano_de_hoje}')

def Baixar_arquivo(data_comp):# URL do PDF que você deseja baixar
    url_do_pdf = rf"https://www.bcb.gov.br/content/focus/focus/R{data_comp}.pdf"

    # Envie uma solicitação HTTP para a URL do PDF
    response = requests.get(url_do_pdf)

    # Verifique se a solicitação foi bem-sucedida (código de resposta 200)
    if response.status_code == 200:
    # Abra um arquivo local em modo de gravação binária (modo 'wb') para salvar o PDF
        with open(rf'{datetime.date.today()}.pdf', 'wb') as file:
            file.write(response.content)
        print('PDF baixado com sucesso.')
    else:
        print('Falha ao baixar o PDF. Código de resposta:', response.status_code)

