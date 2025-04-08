import pandas as pd
import os

class ArmazenarDados():

    def gerar_csv_links(self, dados: list[str]) -> None:
        """
        Armazena os dados coletados durante o processo de scraping em um arquivo CSV.

        Retorna:
        --------
        None
        """
        dados = pd.DataFrame(dados, columns=['links'])

        data_directory = "data"
        os.makedirs(data_directory, exist_ok=True)

        dados.to_csv(
            os.path.join(data_directory, "links-aptos.csv"),
            sep=";",
            encoding="utf-8",
            header=True,
            index=False,
        )