class Bagagem:
    def __init__(self, bilhete, identificacao="", peso=0.0) -> None:
        self.identificacao = identificacao
        self.peso = peso
        self.bilhete = bilhete
    
class Passageiro:
    def __init__(self, nome="", rg="", passageiro=None) -> None:
        self.nome = nome
        self.rg = rg

class Onibus:
    def __init__(self, placa = "", anoFabricacao = 2000, bagageiro = 1.0,
                  totalAssentos = 20, totalLeitos = 5, empresas=[], bilhetes=[]) -> None:
        self.placa = placa
        self.anoFabricacao = anoFabricacao
        self.bagageiro = bagageiro
        self.totalAssentos = totalAssentos
        self.totalLeitos = totalLeitos
        self.empresas = empresas
        self.bilhetes = bilhetes

class Empresa:
    def __init__(self, nome="", anoFundacao=2000, cnpj="", guiches=[]) -> None:
        self.nome = nome
        self.anoFundacao = anoFundacao
        self.cnpj = cnpj
        self.guiche = guiches

class Guiche:
    def __init__(self, numero=0, area=0.0, empresas=[]) -> None:
        self.numero = numero
        self.area = area
        self.empresas = empresas

class Rodoviaria:
    def __init__(self, cidade="", endereco="", guiches=[],) -> None:
        self.cidade = cidade
        self.endereco = endereco
        self.guiches = guiches

class Bilhete:
    def __init__(self, poltrona=1, saida=None, chegada=None, passageiro=None, origem=None, destino=None, onibus=None) -> None:
        self.poltrona = poltrona
        self.saida = saida
        self.chegada = chegada
        self.passageiro = passageiro
        self.origem = origem
        self.destino = destino
        self.onibus = onibus
    
if __name__ == "__main__":
    b = Bagagem(Bilhete(), 123)
    print(b.bilhete.poltrona)