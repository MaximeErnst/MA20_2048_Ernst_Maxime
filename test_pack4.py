# Fonction qui compresse et fusionne 4 cases comme dans le jeu 2048
# Les valeurs sont traitées de gauche à droite
def pack4(a, b, c, d):
    
    # Si la troisième case est vide, on décale la quatrième
    if c == 0:
        c = d
        d = 0

    # Si la deuxième case est vide, on décale les suivantes
    if b == 0:
        b = c
        c = d
        d = 0


    # Si la première case est vide, on décale toutes les valeurs vers la gauche
    if a == 0:
        a = b
        b = c
        c = d
        d = 0

    # Fusion des deux premières cases si elles sont identiques
    if a == b:
        a = a * 2
        b = c
        c = d
        d = 0

    # Fusion des deuxième et troisième cases si identiques
    if b == c:
        b = b * 2
        c = d
        d = 0

    # Fusion des troisième et quatrième cases si identiques
    if c == d:
        c = c * 2
        d = 0

    # Retourne les nouvelles valeurs après compression et fusion
    return a, b, c, d


# Tests de la fonction pack4 pour vérifier son comportement
print(pack4(2, 8, 4, 4))
print(pack4(2, 2, 2, 2))
print(pack4(2, 0, 4, 4))
print(pack4(0, 0, 4, 0))