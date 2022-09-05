def numeroPrimo(num):
    if num == 1:
        return "No es numero primo"
    elif num % 2 == 1:
        return "Es un numero primo"
    else:
        return "No es un numero primo"
    

resultado = numeroPrimo(6)
print(resultado)

