#5. Status do Personagem (10 pontos): Ao inspecionar um personagem (print(meu_guerreiro)),
#  queremos ver um resumo claro de suas informações. Como você pode fazer isso acontecer?

class Guerreiro:
  def __init__(self, nome, pontos_vida, forca_ataque ):
    self.nome = nome
    self.pontos_vida = pontos_vida
    self.forca_ataque = forca_ataque

  def __str__(self):
    return f"Guerreiro: {self.nome}, Vida: {self.pontos_vida}, Ataque: {self.forca_ataque}"
  
meu_guerreiro = Guerreiro("Gustavo", 100, 15)
print(meu_guerreiro)