#3. O Arqueiro (10 pontos): Complete o trio de heróis com um Arqueiro. 
# Pense em um atributo que o diferencie, como sua precisão, e modele a classe correspondente.


class Arqueiro:
  def __init__(self, nome, pontos_vida, forca_ataque, precisao):
    self.nome = nome
    self.pontos_vida = pontos_vida
    self.forca_ataque = forca_ataque
    self.precisao = precisao

arqueiro1 = Arqueiro("Gustavo", "76", "54", "99" ) 
print(f"O arqueiro {arqueiro1.nome}, possui {arqueiro1.pontos_vida} pontos de vida, {arqueiro1.forca_ataque} forca de ataque, e {arqueiro1.precisao} pontos de precisao. Boa batalha!")
    