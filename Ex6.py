def contar_divisiveis_por_5(n):
    contador = 0
    for i in range(1, n + 1):
        if i % 5 == 0:
            contador += 1
    return contador


numero_limite = int(input("Digite o valor de n: "))

resultado = contar_divisiveis_por_5(numero_limite)

print(f"Quantidade de números divisíveis por 5 entre 1 e {numero_limite}: {resultado}")