#DESAFIO FÁCIL
print("nome")

#foi não foi declarado como string dentro do print e sim como uma variavel, por isso o erro.

"""print(nome)"""

##Desafio médio

numeros = [10, 2]
indice = int(input("Digite um índice para acessar a lista: ")) 
if len(numeros) < indice:
    raise IndexError("O valor informado excede a quantidade de index existentes, digite um valor válido")
try:
    print(numeros[indice])
except IndexError as e:
    print(e)

"""numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])"""



##Desafio dificil

def validar_idade(idade: int):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"
try:
    idade = int(input("Digite sua idade: "))
    print(validar_idade(idade))
except ValueError as e:
    print(e)

"""def validar_idade(idade)
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))"""



##Desafio extra

def calcular_media(notas: int) -> int:
    soma = sum(notas)
    if len(notas) > 0:
        quantidade = len(notas)
        return soma / quantidade
    raise Exception("Deve ser informado pelo menos uma nota para o cálculo da média")
try:
    notas = [1,2,3,4]
    media = calcular_media(notas)
    print(f"Média: {media:.2f}")
except Exception as e:
    print(e)

"""def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

notas = [8, 9, "10", 7]
media = calcular_media(notas)
print(f"Média: {media:.2f}")"""