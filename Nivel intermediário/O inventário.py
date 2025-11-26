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

inventario_do_heroi = Inventario()
espada = Arma("Espada Curta", 10)
pocao_vida = Pocao("Poção de Vida", 25)

inventario_do_heroi.adicionar_item(espada)
inventario_do_heroi.adicionar_item(pocao_vida)
inventario_do_heroi.adicionar_item(Pocao("Poção Fraca", 10))

print(f"Itens no inventário: {len(inventario_do_heroi.itens)}")
print(f"Primeiro item: {inventario_do_heroi.itens[0].nome}")
inventario_do_heroi.remover_item(espada)
print(f"Itens restantes: {len(inventario_do_heroi.itens)}")