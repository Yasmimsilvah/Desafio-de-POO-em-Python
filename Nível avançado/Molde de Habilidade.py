from abc import ABC, abstractmethod

class Habilidade(ABC):
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo 

    @abstractmethod
    def usar(self, atacante, alvo):
        pass

class AtaqueBasico(Habilidade):
    def __init__(self):
        super().__init__("Ataque Básico", 0)

    def usar(self, atacante, alvo):
        dano = atacante.forca_base
        print(f"\n{atacante.nome} usa {self.nome} contra {alvo.nome}!")
        alvo.receber_dano(dano)