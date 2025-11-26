import random

class Dado:
    @staticmethod
    def rolar(faces=6):
        return random.randint(1, faces)

d4 = Dado.rolar(4)
d6 = Dado.rolar(6)
d20 = Dado.rolar(20)

print(f"Resultado de um D4: {d4}")
print(f"Resultado de um D6 (padrão): {d6}")
print(f"Resultado de um D20: {d20}")