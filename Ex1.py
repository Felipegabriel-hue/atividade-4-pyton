def numeros(n1,n2):
    resultado = n1 * n2
    return resultado


valor1 = float(input("Digite o primeiro valor: "))

valor2 = float(input("Digite o segundo valor: "))
total_multiplicacao = numeros(valor1, valor2)

print(f"O resultado da multiplicação é: {total_multiplicacao}")