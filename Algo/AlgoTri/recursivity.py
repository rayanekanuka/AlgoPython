def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)

# Exemple d'utilisation
n = 5
resultat = factorielle(n)
print(resultat)   # ici 120


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(8))


def syracuse(n):
    print(n)
    if n > 1:
        if n%2 == 0:
            return syracuse(n/2)
        else:
            return syracuse(3 * n + 1)

print(syracuse(15))

