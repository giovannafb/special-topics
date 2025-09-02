class Avaliacao:
    nota_minima : float  = 6.6
    def __init__(self, matricula="", presenca=0, nota1=0.0, nota2=0.0, sub=0.0) -> None:
        self.matricula : float = matricula
        self.presenca : float = presenca
        self.nota1 : float = nota1
        self.nota2: float = nota2
        self.substituva: float = sub

    def media(self) -> float:
        v = (self.nota1 + self.nota2)/2
        if v < Avaliacao.nota_minima:
            if self.nota1 < self.nota2:
                v = (self.sub + self.nota2)/2
            else:
                v = (self.nota1 + self.sub)/2

        return v
    
    def aprovado(self) -> bool:
        if self.media() >= Avaliacao.nota_minima:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Avaliacao("a123", 0.0, 7.0, 7.0)
    Avaliacao.nota_minima = 5.0
    a2 = Avaliacao("456", nota1=8.0, nota2=8.0)
    Avaliacao.nota_minima = 4.0

    print(a.matricula, a.nota_minima)
    print(a2.matricula, a2.nota_minima)