import math
class FiguraGeometrica:

    @staticmethod
    def AreaCirculo(raio):
        return math.pi * math.pow(raio, 2)
    
    @staticmethod
    def AreaTriangulo(base, altura):
        return (base*altura)/2
    
    @staticmethod
    def HipotenusaTrianguloRetangulo(cateto1, cateto2):
        return math.sqrt((math.pow(cateto1, 2)) + ((math.pow(cateto2, 2))))

