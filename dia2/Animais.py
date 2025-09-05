class Animal:
    def falar(self):
        return "Som animal genérico"
class Gato(Animal):
    def falar(self):
        return "Miau!"
class Cachorro(Animal):
    def falar(self):
        return "Auau!"