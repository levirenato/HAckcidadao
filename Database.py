import pandas as pd


class Database:
    # BASE DE DADOS #
    def __init__(self, link):
        self.__link = link
        self.__data = pd.read_csv(self.__link, index_col=None,sep="|")

    def filtra_lista(self, valor):
        filtrado = self.__data['{}'.format(valor)].drop_duplicates()
        return [i for i in filtrado]

    def soma_lista(self, col_unica, lista, col_soma):
        conta = [self.__data.query(f'{col_unica} == "{i}"')[col_soma].sum() for i in lista]
        return conta

    def soma_item(self, col_soma):
        soma = self.__data['{}'.format(col_soma)].sum()
        return soma

    @property
    def show(self):
        print(self.__data)



