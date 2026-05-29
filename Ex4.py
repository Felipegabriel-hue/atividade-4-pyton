def numero_perfeito(numero):
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    
    if soma_divisores == numero:
        return True
    else:
        return False


num = int(input("Digite um número inteiro: "))

if numero_perfeito(num):
    print(f"O número {num} é perfeito!")
else:
    print(f"O número {num} não é perfeito.")