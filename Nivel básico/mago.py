#2. O Mago (10 pontos): O próximo herói é um Mago. Crie uma classe para ele, considerando que, 
# além das características básicas, ele também possui poder mágico.

class Mago:
  def __init__(self, nome, pontos_vida, forca_ataque, magia):
    self.nome = nome
    self.pontos_vida = pontos_vida
    self.forca_ataque = forca_ataque
    self.magia = magia

mago1 = Mago("Gustavo", "87", "69", "100")
print(f"O mago {mago1.nome} possui {mago1.pontos_vida} pontos de vida, {mago1.forca_ataque} de forca de ataque e {mago1.magia} de magia.")
    