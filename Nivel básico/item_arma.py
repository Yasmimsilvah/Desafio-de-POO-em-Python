#7. Itens: Arma (10 pontos): Um RPG precisa de itens. 
# Crie uma classe para representar uma Arma, que deve ter ao menos
#  um nome e um poder de dano. Crie instâncias para uma "Espada Longa" e um "Cajado Mágico".

class Arma:
  def __init__(self, nome, poder_dano):
    self.nome = nome
    self.poder_dano = poder_dano

espada_longa = Arma("Espada Bastarda", 10)
cajado_magico = Arma("Cajado de fogo", 12)

print(espada_longa.nome)
print(espada_longa.poder_dano)

print(cajado_magico.nome)
print(cajado_magico.poder_dano)
