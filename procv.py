from ler_csv import Ler_csv


def consulta_codigos():

    busca_um = '9'
    busca_dois = 'TESTE 9'

    consul = Ler_csv()
    consul.lendo_csv()
    cod = consul.procv_base(busca_um, busca_dois)
    return cod

print(consulta_codigos())
