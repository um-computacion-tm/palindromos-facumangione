def is_palindrome(value):
    for indice in range(len(value) // 2):  # Utiliza // para la división entera
        reverse = -(indice + 1)
        if value[indice] != value[reverse]:
            return False
    return True