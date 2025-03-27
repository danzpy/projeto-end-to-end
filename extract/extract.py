from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def configuracao_driver() -> Options:
    """
    Configura as opções do driver Chrome para execução em ambiente headless e com algumas opções de
    desempenho desabilitadas, como GPU e 3D APIs.

    Returns:
        Options: Configurações do ChromeDriver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-3d-apis")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--headless")

    return chrome_options


def chrome_com_espera(driver: WebDriver, segundos: int) -> WebDriverWait:
    """
    Cria uma instância do WebDriverWait com base no driver fornecido e um tempo de espera.

    Args:
        driver (WebDriver): Instância do driver do Selenium.
        segundos (int): Tempo em segundos para o qual o WebDriverWait aguardará por um elemento.

    Returns:
        WebDriverWait: Instância do WebDriverWait configurada.
    """
    return WebDriverWait(driver, segundos)


def inicializando_chrome(settings: Options) -> WebDriver:
    """
    Inicializa o ChromeDriver com as configurações fornecidas e acessa a URL especificada.

    Args:
        settings (Options): Configurações personalizadas do ChromeDriver.

    Returns:
        WebDriver: Instância do WebDriver do Chrome com a página carregada.
    """

    url = 'https://www.hostelworld.com/hostels/south-america/brazil/sao-paulo/'

    driver = webdriver.Chrome(options=settings)
    driver.get(url)

    return driver

settings = configuracao_driver()
driver = inicializando_chrome(settings)
driver_set = chrome_com_espera(driver, segundos=10)

containers = driver_set.until(
    EC.presence_of_all_elements_located((
        By.XPATH,
        ".//a[contains(@class, 'property-card-container') and contains(@class, 'property-listing-card')]"
    ))
)

for info in containers:
    elemento = info.find_element(By.XPATH, ".//div[contains(@class, 'property-name')]")
    print(elemento.text)