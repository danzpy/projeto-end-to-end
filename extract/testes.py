from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar o driver
options = Options()
#options.add_argument("--headless")  # Você pode remover essa linha se quiser ver o navegador
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
url = 'https://casa.sapo.pt/comprar-apartamento-t2-porto-paranhos-74da44a3-0a65-11f0-9e61-060000000056.html?g3pid=1016288'
driver.get(url)
map = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        ".//div[contains(@id, 'objMap')]"
    ))
)

lat = map.get_attribute('data-latitude')
long = map.get_attribute('data-longitude')

print(lat, long)