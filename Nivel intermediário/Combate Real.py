class Personagem:
    def __init__(self, nome, vida_maxima, forca_base):
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.forca_base = forca_base
        self._vida = vida_maxima 

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
        dano_causado = self.forca_base
        
        print(f"\n{self.nome} ataca {alvo.nome} causando {dano_causado} de dano!")
        alvo.receber_dano(dano_causado)


class Guerreiro(Personagem):
    def __init__(self, nome, vida_maxima, forca_base, defesa):
        super().__init__(nome, vida_maxima, forca_base)
        self.defesa = defesa

guerreiro_a = Guerreiro("Heroi", 100, 20, 5)
guerreiro_b = Guerreiro("Vilao", 50, 10, 3)

print(f"--- Início do Combate ---")

guerreiro_a.atacar(guerreiro_b) 

guerreiro_b.atacar(guerreiro_a)

print(f"\n--- Fim da Rodada ---")
print(f"Vida Heroi: {guerreiro_a.get_vida()}")
print(f"Vida Vilao: {guerreiro_b.get_vida()}")