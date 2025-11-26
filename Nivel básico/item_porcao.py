#8. Itens: Poção (10 pontos): Crie também uma classe para representar uma Poção.
#  Ela deve ter um nome e um valor de cura. Crie uma instância para uma "Poção de Vida".

class Porcao:
  def __init__(self, nome, vlr_cura):
    self.nome = nome
    self.vlr_cura = vlr_cura

porcao_vida = Porcao("porcao de cura", 25)

print (f"Beba a {porcao_vida.nome} que tem a cura de {porcao_vida.vlr_cura}")
