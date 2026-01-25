import pandas as pd
import os

class FormatoArmazenamento:
    """
    Classe base para diferentes formatos de armazenamento de dados.
    Contém o método para armazenar arquivos no formato CSV.
    """

    def armazenar_csv(self, df: pd.DataFrame, diretorio: str, nome_arquivo: str) -> str:
        """
        Armazena um DataFrame como um arquivo CSV no diretório e nome de arquivo especificados.

        Parâmetros:
        -----------
        df : pd.DataFrame
            DataFrame que será salvo.
        diretorio : str
            Caminho do diretório onde o arquivo será salvo.
        nome_arquivo : str
            Nome do arquivo CSV a ser criado.

        Retorna:
        --------
        str
            Representação do CSV como string.
        """
        dados_transformados = df.to_csv(
            os.path.join(diretorio, nome_arquivo),
            sep=";",
            encoding="utf-8",
            header=True,
            index=False,
        )

        return dados_transformados


class Armazenamento(FormatoArmazenamento):
    """
    Classe responsável por gerenciar o armazenamento de dados em disco.

    Atributos:
    ----------
    diretorio : str
        Caminho do diretório onde os dados serão salvos.
    """

    def __init__(self, diretorio: str) -> None:
        """
        Inicializa a instância com o diretório de destino.

        Parâmetros:
        -----------
        diretorio : str
            Caminho do diretório onde os arquivos serão armazenados.
        """
        self.diretorio = diretorio

    def checa_diretorio(self) -> None:
        """
        Verifica se o diretório existe. Se não existir, cria.
        """
        os.makedirs(self.diretorio, exist_ok=True)
    
    def gerar_csv(self, dados, nome_arquivo: str, deduplicar_por: str):

        df = pd.DataFrame(dados)

        if deduplicar_por is not None:
            df = df.drop_duplicates(subset=[deduplicar_por])

        self.checa_diretorio()
        self.armazenar_csv(df=df, diretorio=self.diretorio, nome_arquivo=nome_arquivo)
