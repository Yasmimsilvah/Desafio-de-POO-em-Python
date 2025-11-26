class Personagem:
    def __init__(self, nome, vida_maxima, forca_base):
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima  
        self.forca_base = forca_base

class Guerreiro(Personagem):
    """
    Herda de Personagem e adiciona um atributo específico: defesa.
    """
    def __init__(self, nome, vida_maxima, forca_base, defesa):
        super().__init__(nome, vida_maxima, forca_base)
        
        self.defesa = defesa

heroi = Guerreiro("Conan", 120, 18, 5)

print(f"O Guerreiro {heroi.nome} foi criado com sucesso!")
print(f"Vida Base: {heroi.vida}") 
print(f"Defesa Específica: {heroi.defesa}")