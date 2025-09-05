import FiguraGeometrica
import math

#DESAFIO NIVEL DIFICIL

def retornoFunções(escolha):
    match escolha:
        case 1:
            raio = float(input("Digite o raio do circulo"))
            return print(FiguraGeometrica.AreaCirculo(raio))
        case 2:
            base = float(input("Digite a base"))
            altura = float(input("Digite altura"))
            return print(FiguraGeometrica.AreaTriangulo(base, altura))
        case 3:
            cateto1 = float(input("Digite o primeiro cateto"))
            cateto2 = float(input("Digite o segundo cateto"))
            return print(FiguraGeometrica.HipotenusaTrianguloRetangulo(cateto1, cateto2))
        
print("Digite o número da area que deseja cálcular.")

print("1- area do circulo")
print("2- area do triangulo")
print("3- area do triangulo retangulo")

escolha = int(input())
if (escolha > 3) or (escolha < 0):
    print("insira um valor válido")    

retornoFunções(escolha)    

#FIM DESAFIO NIVEL DIFICIL




