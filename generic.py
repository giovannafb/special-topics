from __future__ import annotations
from abc import ABC, abstractmethod
from math import sqrt
from typing import Any

class Localizacao(ABC):
    @abstractmethod
    def __init__(self, latitude: float = 0.0, longitude: float = 0.0) -> None:
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude

class Afericao[T: Afericao](ABC):
    @abstractmethod
    def distancia(self, obj: T) -> float:
        pass

class Prototipo[T: Prototipo](ABC):
    @abstractmethod
    def clone(self) -> T:
        pass

class Cidade(Localizacao, Afericao[Any], Prototipo[Any]):
    def __init__(self, latitude: float = 0.0, longitude: float = 0.0, nome: str = "") -> None:
        super().__init__(latitude, longitude)
        self.nome = nome

    def distancia(self, obj: Cidade) -> float:
        return sqrt((self.latitude-obj.latitude)**2 + (self.longitude-obj.longitude)**2)
    
    def clone(self) -> Cidade:
        return Cidade(self.latitude, self.longitude, self.nome)

    def getNome(self) -> str:
        return self.nome
    
    def setNome(self, v: str = ""):
        self.nome = v


if __name__ == "__main__":
    c1 = Cidade(1.0, 1.0, "Itajuba")
    print(c1, c1.__dict__)
    c2 = c1.clone()
    print(c2, c2.__dict__)
    c3 = Cidade(2.0, 2.0, "Piranguinho")
    print(c1.distancia(c3))