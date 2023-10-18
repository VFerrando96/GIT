from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
import time
def abrir_site_e_buscar(url):
    
    driver.get(url)
    xpath = "/html/body/app-root/app-root/div/div/main/dynamic-comp/div/div[1]/bcb-publicacao/div/div[1]/div/div/div[2]"  # Replace with your specific XPath
    wait = WebDriverWait(driver, 5)  
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    element_text = element.text
    driver.quit()
    print("Element Text:", element_text)


