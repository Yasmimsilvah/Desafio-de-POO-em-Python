class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            return True
        return False

class Personagem:
    def __init__(self, nome, vida_maxima, forca_base):
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.forca_base = forca_base
        self._vida = vida_maxima
        self.inventario = Inventario() 

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

heroi = Guerreiro("Conan", 100, 15, 5)
pocao = Pocao("Poção de Cura Média", 50)

heroi.inventario.adicionar_item(pocao)
heroi.inventario.adicionar_item(Arma("Machado", 10))

print(f"O Guerreiro {heroi.nome} tem {len(heroi.inventario.itens)} itens.")
print(f"O primeiro item é: {heroi.inventario.itens[0].nome}")