#6. Ação de Ataque (10 pontos): Personagens e monstros precisam de uma ação básica: 
# atacar. Adicione um comportamento de ataque às suas classes.
#  Por enquanto, pode ser uma simples mensagem de ação.

class Guerreiro:
  def __init__(self, nome, pontos_vida, forca_ataque):
    self.nome = nome 
    self.pontos_vida = pontos_vida
    self.forca_ataque = forca_ataque

  def __str__(self):
   return f"Guerreiro: {self.nome}, Vida: {self.pontos_vida}, Ataque: {self.forca_ataque}"

  def atacar(self):
    print(f"{self.nome} ataca com sua espada!")

meu_guerreiro = Guerreiro("Gustavo", 100, 15)
meu_guerreiro.atacar ()
print(meu_guerreiro)
