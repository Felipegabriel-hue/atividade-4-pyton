def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    texto_invertido = texto[::-1]
    
    if texto == texto_invertido:
        return True
    else:
        return False


palavra = input("Digite uma palavra ou frase: ")

if verificar_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")