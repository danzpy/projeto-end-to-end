from extract.extract import CustomOptions, ScraperLinks, ScrapperInfo, DriverManager, ManipuladorArquivos
from load.load import Armazenamento

carregar = Armazenamento(diretorio='data')
options = CustomOptions()
driver = DriverManager(options)

coletor_links = ScraperLinks(driver)
coletor_links.scraping()

csv_links = 'links-aptos-updated.csv'
csv_dados = 'dados-aptos-updated.csv'

carregar.gerar_csv(dados=coletor_links.links_coletados(), deduplicar_por='link', nome_arquivo=csv_links)
links_coletados = ManipuladorArquivos().carregar_dados(diretorio="data", nome_arquivo=csv_links)

coletor_dados = ScrapperInfo(driver, fonte_dados=links_coletados)
coletor_dados.scraping()
carregar.gerar_csv(dados=coletor_dados.dados_coletados(), deduplicar_por='link', nome_arquivo=csv_dados)