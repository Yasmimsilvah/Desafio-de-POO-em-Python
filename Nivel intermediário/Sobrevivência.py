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
        self.equipada = None

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
        print(f"\n{self.nome} realiza um ataque básico contra {alvo.nome} causando {dano_causado} de dano!")
        alvo.receber_dano(dano_causado)
    
    def usar_item(self, item):
        if item in self.inventario.itens:
            if isinstance(item, Pocao):
                nova_vida = self.get_vida() + item.cura
                self.set_vida(nova_vida)
                self.inventario.remover_item(item)
                print(f"[{self.nome}] usou {item.nome} e curou {item.cura} de vida.")
                print(f"Vida atual: {self.get_vida()}")
            else:
                print(f"[{self.nome}] {item.nome} não é um item de cura para ser usado assim.")
        else:
            print(f"[{self.nome}] {item.nome} não está no inventário.")

    def esta_vivo(self):
        return self.get_vida() > 0

class Monstro(Personagem):
    @classmethod
    def criar_goblin_padrao(cls, nome):
        VIDA_PADRAO = 30
        FORCA_PADRAO = 8
        return cls(nome, VIDA_PADRAO, FORCA_PADRAO)

class Guerreiro(Personagem):
    def __init__(self, nome, vida_maxima, forca_base, defesa):
        super().__init__(nome, vida_maxima, forca_base)
        self.defesa = defesa

    def atacar(self, alvo):
        dano_causado = self.forca_base + (self.defesa // 2)
        print(f"\n{self.nome} desfere um poderoso golpe com Força extra contra {alvo.nome} causando {dano_causado} de dano!")
        alvo.receber_dano(dano_causado)

goblin = Monstro.criar_goblin_padrao("Goblin Fraco")

print(f"O Goblin está vivo? {goblin.esta_vivo()}")
goblin.receber_dano(20)
print(f"O Goblin está vivo? {goblin.esta_vivo()}")
goblin.receber_dano(10)
print(f"O Goblin está vivo? {goblin.esta_vivo()}")