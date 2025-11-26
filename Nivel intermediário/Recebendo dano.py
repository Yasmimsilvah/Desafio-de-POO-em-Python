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
            print(f"[{self.nome}] A vida não pode ser menor que zero!")
            self._vida = 0
        elif novo_valor_vida > self.vida_maxima:
            print(f"[{self.nome}] A vida não pode ultrapassar o máximo!")
            self._vida = self.vida_maxima
        else:
            self._vida = novo_valor_vida
            
        return self._vida

    def receber_dano(self, dano):
        nova_vida = self.get_vida() - dano
      
        self.set_vida(nova_vida)
        
        print(f"[{self.nome}] recebeu {dano} de dano. Vida atual: {self.get_vida()}")

class Guerreiro(Personagem):
    def __init__(self, nome, vida_maxima, forca_base, defesa):
        super().__init__(nome, vida_maxima, forca_base)
        self.defesa = defesa

guerreiro = Guerreiro("Arthur", 80, 15, 5)

print(f"Vida inicial de {guerreiro.nome}: {guerreiro.get_vida()}")

guerreiro.receber_dano(30) 

guerreiro.receber_dano(100)

print(f"Vida final de {guerreiro.nome}: {guerreiro.get_vida()}")