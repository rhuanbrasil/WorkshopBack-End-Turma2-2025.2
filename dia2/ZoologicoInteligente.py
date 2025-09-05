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

class zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, Animal):
        zoologico.animais.append(Animal)

    def listar_animais(self):
        if not self.animais:
            return "Sem animais na lista"
        return [a.apresentar() for a in self.animais]
        
    def filtrar_por_tipo(self, tipo):
        return [animal for animal in self.animais if isinstance(animal, tipo)]