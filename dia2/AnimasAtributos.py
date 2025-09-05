class Animal:
    def __init__(self, nome, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return self.nome, self.idade
    
    def falar(self):
        return "Som animal genérico"
    
class Gato(Animal):        
    def falar(self):
        return "Miau!"
class Cachorro(Animal):
    def falar(self):
        return "Auau!"    