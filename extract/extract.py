from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from time import sleep

class CustomOptions:
    """
    Classe responsável por aplicar as configurações do navegador Chrome para o WebDriver.

    Atributos:
    ----------
    chrome_options : Options
        Instância de opções do Chrome configurada com diversos argumentos.
    """

    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-3d-apis")
        self.chrome_options.add_argument("--allow-insecure-localhost")
        self.chrome_options.add_argument("--log-level=3")
        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36"
        )
        self.chrome_options.add_argument("--headless")

    def espera(self, driver) -> WebDriverWait:
        """
        Configura o tempo máximo de espera para que elementos estejam presentes na url especificada antes de interagir com eles.

        Parâmetros:
        -----------
        driver : WebDriver
            Instância do WebDriver que será usada para configurar a espera.

        Retorna:
        --------
        WebDriverWait
            Instância configurada de WebDriverWait.
        """
        self.tempo = 40
        return WebDriverWait(driver, self.tempo)
    
class DriverManager:
    """
    Classe responsável por inicializar e fornecer acesso ao WebDriver e suas configurações.

    Atributos:
    ----------
    __driver : WebDriver
        Instância do navegador configurada com as opções fornecidas.
    __options : CustomOptions
        Instância de opções personalizadas para o navegador.
    """
    def __init__(self, options:CustomOptions) -> None:
        self.__driver = webdriver.Chrome(options=options.chrome_options)
        self.__options = options

    def get_driver(self) -> None:
        """
        Retorna a instância do WebDriver.

        Retorna:
        --------
        WebDriver
        """
        return self.__driver
    
    def get_options(self) -> None:
        """
        Retorna a instância de opções do navegador.

        Retorna:
        --------
        CustomOptions
        """
        return self.__options

class Scraper:
    """
    Classe responsável por gerenciar o navegador e realizar o processo de scraping.

    Depende de instâncias configuradas de WebDriver e CustomOptions, fornecidas por DriverManager.

    Atributos:
    ----------
    driver : WebDriver
        Instância do WebDriver configurada com opções personalizadas.
    options : CustomOptions
        Instância da classe CustomOptions contendo as opções de configuração do navegador.
    pagina : int
        Número da página atual que está sendo processada.
    base_url : str
        URL base do site a ser raspado.
    dados_coletados : dict
        Dicionário que armazena os dados coletados como links dos produtos.
    """
    
    def __init__(self, driver: DriverManager) -> None:
        self.__driver = driver.get_driver()
        self.__options = driver.get_options()
        self.__pagina = 1
        self.base_url = 'https://casa.sapo.pt/comprar-apartamentos/porto/'
        self.__dados_coletados = {"link": []}

    def __acessar_url(self, url=None) -> None:
        """
        Acessa a URL especificada. Se nenhuma URL for passada, acessa a URL padrão configurada com base na página atual.

        Parâmetros:
        -----------
        url : str, opcional
            URL que será acessada. Se não especificada, será gerada a URL padrão baseada na página atual.

        Retorna:
        --------
        None
        """

        if url is None:
            url = f"{self.base_url}?pn={self.__pagina}"
        self.__driver.get(url)

    def __coletar_links(self) -> None:
        """
        Coleta todos os cartões de produtos presentes na página e extrai suas informações.

        Retorna:
        --------
        None
        """
        espera = self.__options.espera(self.__driver)
        aptos = espera.until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                "//div[contains(@class, 'property-info-content')]"
            ))
        )

        for ap in aptos:
            if ap.is_displayed():
                link_element = ap.find_element(By.XPATH, ".//a[contains(@class, 'property-info')]")
                href = link_element.get_attribute("href")
                self.__dados_coletados['link'].append(href)

    def __valida_ultima_pagina(self) -> bool:
        """
        Verifica se a última página de resultados foi alcançada.

        Retorna:
        --------
        bool
            True se a última página foi alcançada, caso contrário False.
        """
        espera = self.__options.espera(self.__driver)
        try:
            ultima_pagina = espera.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//span[contains(@class, 'disabled')]"
                ))
            )

            if ultima_pagina: #and self.pagina != 1  <- Descomentar quando for rodar a coleta:
                logger.info(
                    f"Cheguei na última página: {self.__pagina}.\nDados extraídos com sucesso."
                )
                return True
        except:
            pass

    def __proxima_pagina(self) -> None:
        """
        Avança para a próxima página de resultados e acessa a URL correspondente.

        Retorna:
        --------
        None
        """
        self.__pagina += 1
        proxima_pagina = f"{self.base_url}?pn={self.__pagina}"
        self.__acessar_url(proxima_pagina)

    def scraping_links(self) -> None:
        """
        Executa o processo completo de scraping, passando por todas as páginas disponíveis até a última.

        Retorna:
        --------
        None
        """
        self.__acessar_url()
        while True:
            self.__coletar_links()

            logger.info(f"Coleta da página {self.__pagina} realizada com sucesso..")
            sleep(2)

            if self.__valida_ultima_pagina():
                break
            else:
                self.__proxima_pagina()

    def get_links(self) -> list[str]:
        """
        Retorna a lista de links coletados.

        Retorna:
        --------
        list[str]
        """

        return self.__dados_coletados["link"]