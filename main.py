from extract.extract import CustomOptions, ScraperLinks, ScrapperInfo, DriverManager
from load.load import Armazenamento

carregar = Armazenamento(diretorio='data')
options = CustomOptions()
driver = DriverManager(options)
links = ScraperLinks(driver)
dados = ScrapperInfo(driver)


#links.scraping_links()
#carregar.gerar_csv_links(chrome.get_links())

dados.percorre_links()
carregar.gerar_csv_dados(dados.get_dados())