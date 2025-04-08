from extract.extract import CustomOptions, Navegador
from load.load import ArmazenarDados


options = CustomOptions()
chrome = Navegador(options)

armazenador = ArmazenarDados()

chrome.scraping_links()
armazenador.gerar_csv_links(chrome.get_links())