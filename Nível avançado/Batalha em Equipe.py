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
    def __init__(self, equipe_a, equipe_b):
        self.equipe_a = equipe_a
        self.equipe_b = equipe_b
        
        nomes_a = [p.nome for p in equipe_a]
        nomes_b = [p.nome for p in equipe_b]
        
        print("\n--- INÍCIO DA BATALHA EM EQUIPE ---")
        print(f"Equipe A ({', '.join(nomes_a)}) vs Equipe B ({', '.join(nomes_b)})")

    def _obter_primeiro_vivo(self, equipe):
        for personagem in equipe:
            if personagem.esta_vivo():
                return personagem
        return None

    def _equipe_esta_viva(self, equipe):
        return any(p.esta_vivo() for p in equipe)

    def iniciar_combate(self):
        turno = 1
        
        while self._equipe_esta_viva(self.equipe_a) and self._equipe_esta_viva(self.equipe_b):
            print(f"\n--- TURNO {turno} ---")

            atacante_a = self._obter_primeiro_vivo(self.equipe_a)
            atacante_b = self._obter_primeiro_vivo(self.equipe_b)
            
            alvo_b = self._obter_primeiro_vivo(self.equipe_b)
            alvo_a = self._obter_primeiro_vivo(self.equipe_a)
            
            if atacante_a and alvo_b:
                atacante_a.atacar(alvo_b)

            if atacante_b and alvo_a:
                atacante_b.atacar(alvo_a)

            turno += 1

        print("\n--- FIM DO COMBATE ---")
        
        if self._equipe_esta_viva(self.equipe_a):
            print("VITÓRIA! A Equipe A venceu!")
            return self.equipe_a
        elif self._equipe_esta_viva(self.equipe_b):
            print("VITÓRIA! A Equipe B venceu!")
            return self.equipe_b
        else:
            print("EMPATE! Ambas as equipes foram derrotadas.")
            return []