from extract.extract import CustomOptions, Scraper, DriverManager
from load.load import Armazenamento


options = CustomOptions()
driver = DriverManager(options)
chrome = Scraper(driver)

carregar = Armazenamento('data')

chrome.scraping_links()
carregar.gerar_csv_links(chrome.get_links())