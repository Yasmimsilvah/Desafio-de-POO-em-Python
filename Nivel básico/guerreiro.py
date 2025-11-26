#1. O Guerreiro (10 pontos): Precisamos representar um Guerreiro. 
# Pense nas características essenciais que ele deve ter (como nome, pontos de vida, força de ataque)
# e crie uma classe para representá-lo.

class Guerreiro:
  def __init__(self, nome, pontos_vida, forca_ataque ):
    self.nome = nome
    self.pontos_vida = pontos_vida
    self.forca_ataque = forca_ataque

primeiro_guerreiro = Guerreiro("Gustavo", "100", "165")
print(f"O nosso guerreiro {primeiro_guerreiro.nome}, possui {primeiro_guerreiro.pontos_vida} pontos de vida, e {primeiro_guerreiro.forca_ataque} de forca de ataque")
