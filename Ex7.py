def contar_digitos(numero):
    if numero == 0:
        return 1
    
    if numero < 0:
        numero = -numero
        
    contador = 0
    while numero > 0:
        numero = numero // 10
        contador += 1
        
    return contador


num_inteiro = int(input("Digite um número inteiro: "))

quantidade_digitos = contar_digitos(num_inteiro)

print(f"O número tem {quantidade_digitos} dígitos.")