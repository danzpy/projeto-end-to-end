from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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
elem_carac = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//div[contains(@class, 'detail-section') and contains(@class, 'detail-features')]"
    ))
)

# Coleta os botões (abas) do menu lateral
menu = elem_carac.find_element(By.XPATH, ".//div[contains(@class, 'detail-features-menu-content')]")
botoes = menu.find_elements(By.TAG_NAME, "span")

# Loop por cada aba
for botao in botoes:
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
        sleep(0.5)

        # Clica via JavaScript para evitar erro de interceptação
        driver.execute_script("arguments[0].click();", botao)
        print(f"\nClicado: {botao.text.upper()}")


        menu_items = elem_carac.find_element(By.XPATH, ".//div[contains(@class, 'detail-features-items')]")
        items = menu_items.find_elements(By.XPATH, ".//div[contains(@class, 'detail-features-item')]")

        for item in items:
            print(item.text)
    except:
        print('Deu ruim')
