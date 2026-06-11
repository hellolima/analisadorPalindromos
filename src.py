import unicodedata

def sanitizar(frase):
    frase = ''.join(filter(str.isalnum, frase))
    frase = frase.lower()
    return frase

def eh_palindromo(frase):
    return sanitizar(frase) == sanitizar(frase)[::-1]

if __name__ == "__main__":
    ehPalindromo = False

    while(True):

        frase = input("Informe a palavra que você deseja verificar (Ctrl+C para sair): ")

        if eh_palindromo(frase):
            ehPalindromo = True
            print(f"{frase} é um palíndromo.")
        else:
            ehPalindromo = False
            print(f"{frase} não é um palíndromo.")