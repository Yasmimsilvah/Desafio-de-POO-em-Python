#10. Poder de Ataque Real (10 pontos): O ataque de um herói deve considerar 
# sua força base mais o poder da arma equipada. Atualize a lógica de ataque para refletir essa soma.

class Arma:
  def __init__(self, nome, poder_dano):
    self.nome = nome
    self.poder_dano = poder_dano

class Guerreiro:
  def __init__(self, nome, pontos_vida, forca_base, arma_guerreiro):
    self.nome = nome
    self.pontos_vida = pontos_vida
    self.forca_base = forca_base
    self.arma = arma_guerreiro

  def atacar(self):
    dano_total = self.forca_base + self.arma.poder_dano

    print(f"{self.nome} ataca com seu/sua {self.arma.nome}")
    print(f"Forca base {self.forca_base} + Dano da arma {self.arma.poder_dano}")

    print(f"Dano total: {dano_total}")