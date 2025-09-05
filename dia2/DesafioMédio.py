import math

#DESAFIO MÉDIO
def arredondamentos(num: float) -> dict:
    return {
        "baixo": math.floor(num),
        "cima": math.ceil(num), 
        "Arredondado": round(num)
    }

num = float(input("Digite o valor a ser arredondado:"))
print(arredondamentos(num))