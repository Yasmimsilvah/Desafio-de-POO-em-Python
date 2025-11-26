import random
from abc import ABC, abstractmethod

class Dado:
    @staticmethod
    def rolar(faces=6):
        return random.randint(1, faces)

class Personagem:
    def __init__(self, nome, vida_maxima, forca_base):
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.forca_base = forca_base
        self._vida = vida_maxima
        self.inventario = None
        self.equipada = None
        self.habilidades = []

    def get_vida(self):
        return self._vida

    def set_vida(self, novo_valor_vida):
        if novo_valor_vida < 0:
            self._vida = 0
        elif novo_valor_vida > self.vida_maxima:
            self._vida = self.vida_maxima
        else:
            self._vida = novo_valor_vida
            
        return self._vida

    def receber_dano(self, dano):
        nova_vida = self.get_vida() - dano
        self.set_vida(nova_vida)
        
        print(f"[{self.nome}] recebeu {dano} de dano. Vida atual: {self.get_vida()}")

    def atacar(self, alvo):
        dado_dano = Dado.rolar(4) 
        dano_total = self.forca_base + dado_dano
        print(f"\n{self.nome} ataca {alvo.nome} (Dano Base: {self.forca_base} + D4: {dado_dano}) causando {dano_total} de dano!")
        alvo.receber_dano(dano_total)
    
    def esta_vivo(self):
        return self.get_vida() > 0

class Monstro(Personagem):
    @classmethod
    def criar_goblin_padrao(cls, nome):
        VIDA_PADRAO = 30
        FORCA_PADRAO = 8
        return cls(nome, VIDA_PADRAO, FORCA_PADRAO)

class Orc(Monstro):
    def __init__(self, nome, vida_maxima, forca_base, chance_critica):
        super().__init__(nome, vida_maxima, forca_base)
        self.chance_critica = chance_critica 

    def atacar(self, alvo):
        dado_sorte = Dado.rolar(100)
        dano_base_ataque = self.forca_base + Dado.rolar(6)
        
        if dado_sorte <= self.chance_critica:
            dano_causado = dano_base_ataque * 2
            print(f"\nCRÍTICO! {self.nome} ESMAGA {alvo.nome} ({dano_base_ataque} x 2) causando {dano_causado} de dano!")
        else:
            dano_causado = dano_base_ataque
            print(f"\n{self.nome} ataca {alvo.nome} causando {dano_causado} de dano.")

        alvo.receber_dano(dano_causado)

orc = Orc("Grug, o Cruel", 150, 25, 20)
guerreiro = Personagem("Arthur", 100, 15)

print(f"Vida de Arthur: {guerreiro.get_vida()}")
orc.atacar(guerreiro)
orc.atacar(guerreiro) 
orc.atacar(guerreiro) 
print(f"Vida de Arthur após ataques: {guerreiro.get_vida()}")