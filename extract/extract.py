from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-3d-apis")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
)

url = 'https://www.hostelworld.com/hostels/south-america/brazil/sao-paulo/'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

containers = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((
        By.XPATH,
        ".//a[contains(@class, 'property-card-container') and contains(@class, 'property-listing-card')]"
    ))
)

for info in containers:
    elemento = info.find_element(By.XPATH, ".//div[contains(@class, 'property-name')]")
    print(elemento.text)