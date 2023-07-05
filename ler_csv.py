import os

import pandas as pd

nome_arqv = os.path.dirname(os.path.abspath(__file__))
pasta = os.path.join(nome_arqv, 'static')

class Ler_csv:
    def __init__(self):
        self.df_base = None

    def lendo_csv(self):
        try:
            self.df_base = pd.read_csv(
                os.path.join(pasta, 'base.csv'),
                delimiter=';')
        except Exception as e:
            print(e)

    def procv_base(self, busca1, busca2):

        if self.df_base is None:
            return None, None
        df2 = self.df_base[
            (self.df_base['codigo'] == busca1) &
            (self.df_base['descricao'] == busca2)]
        if df2 is not None:
            return df2['codigo'].values[0], df2['descricao'].values[0], df2['tipo'].values[0]
        return None, None

