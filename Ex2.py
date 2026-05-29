
def calcular_raiz(n, x):
    resultado = n ** (1 / x)
    return resultado
radicando = float(input("Digite o valor do radicando (n): "))
ordem = float(input("Digite a ordem da raiz (x): "))
raiz_final = calcular_raiz(radicando, ordem)
print(f"O resultado da raiz é: {raiz_final:.2f}")