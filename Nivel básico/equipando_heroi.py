#9. Equipando um Herói (10 pontos): Um guerreiro é mais forte com uma arma.
#  Como você pode associar um objeto Arma a um personagem, como o Guerreiro?

class Arma:
  def __init__(self, nome, poder_dano):
    self.nome = nome
    self.poder_dano = poder_dano

class Guerreiro:
    def __init__(self, nome, pontos_vida, arma_guerreiro):
      self.nome = nome
      self.pontos_vida = pontos_vida
      self.arma = arma_guerreiro
  
espada_longa = Arma("Espada Bastarda", 30)
machado_grande = Arma("Machado de Assis", 67)

guerreiro1 = Guerreiro("Gohan", 100, espada_longa)
guerreiro2 = Guerreiro("Kratos", 243, machado_grande)

print(f"O guerreiro {guerreiro1.nome} esta usando a arma {guerreiro1.arma.nome}")
print(f"A arama de {guerreiro2.nome} e {guerreiro2.arma.nome} e tem {guerreiro2.arma.poder_dano} de dano")