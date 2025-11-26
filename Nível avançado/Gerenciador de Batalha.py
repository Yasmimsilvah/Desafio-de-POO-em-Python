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

class Batalha:
    def __init__(self, combatente_a, combatente_b):
        if not isinstance(combatente_a, Personagem) or not isinstance(combatente_b, Personagem):
            raise TypeError("Ambos combatentes devem ser instâncias de Personagem.")
            
        self.combatente_a = combatente_a
        self.combatente_b = combatente_b
        
        print("\n--- INÍCIO DA BATALHA ---")
        print(f"{self.combatente_a.nome} vs {self.combatente_b.nome}")

heroi = Personagem("Heroi", 100, 15)
vilao = Personagem("Vilão", 80, 12)

confronto = Batalha(heroi, vilao)