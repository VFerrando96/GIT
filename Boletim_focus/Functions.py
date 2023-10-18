from selenium import webdriver
import time
def abrir_site_e_esperar(url, tempo_em_segundos=15):
    driver = webdriver.Chrome()  # Substitua 'Chrome' pelo navegador de sua escolha
    driver.get(url)
    time.sleep(tempo_em_segundos)
    driver.quit()