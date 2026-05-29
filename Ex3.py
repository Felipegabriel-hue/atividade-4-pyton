def calcular_area_quadrado(b):
    area = b ** 2
    return area


base = float(input("Digite o valor da base do quadrado: "))

resultado_area = calcular_area_quadrado(base)

print(f"A área do quadrado é: {resultado_area}")