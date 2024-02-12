def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)

# Exemple d'utilisation
n = 5
resultat = factorielle(n)
print(resultat)   # ici 120


