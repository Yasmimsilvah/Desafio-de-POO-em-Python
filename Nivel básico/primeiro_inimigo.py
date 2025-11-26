#4. O Primeiro Inimigo (10 pontos): Todo herói precisa de um adversário.
#  Crie uma classe para representar um Monstro genérico e, a partir dela, 
# crie uma instância de um Goblin,o primeiro desafio da jornada.

class Inimigo:
  def __init__(self, nome, pontos_vida, ataque):
    self.nome = nome 
    self.pontos_vida = pontos_vida
    self.ataque = ataque

goblin = Inimigo("Astolfo", "39", "71")
print(f"O nosso inimigo {goblin.nome}, possui {goblin.pontos_vida} pontos de vida e {goblin.ataque} pontos de ataque. Que o melhor ganhe a batalha!")
    