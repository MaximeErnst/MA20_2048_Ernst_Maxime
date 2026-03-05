# Dictionnaire associant chaque valeur du jeu 2048 à une couleur spécifique
# La clé correspond au nombre affiché dans la case
# La valeur correspond au code couleur HEX utilisé pour le fond du label

colors = {

    0: "#DBD4CA",  # Case vide (couleur neutre beige/gris)

    2: "#FF9999",  # Rouge clair
    4: "#FFCC99",  # Orange clair
    8: "#FFFF99",  # Jaune clair
    16: "#CCFF99",  # Vert clair
    32: "#99FF99",  # Vert plus soutenu
    64: "#99FFCC",  # Vert menthe
    128: "#99FFFF",  # Cyan clair
    256: "#99CCFF",  # Bleu clair
    512: "#9999FF",  # Bleu moyen
    1024: "#CC99FF",  # Violet clair
    2048: "#FF99FF",  # Rose / Magenta clair
    4096: "#FFCCE6",  # Rose pâle
    8192: "#6600CC",  # Violet foncé (grande valeur)

}

# Matrice représentant l'état du jeu 2048
# Chaque nombre correspond à la valeur d'une case
game = [[4, 0, 2, 2],
        [2, 2, 0, 0],
        [0, 2, 2, 4],
        [4, 4, 2, 4]]

# Liste 2D vide qui contiendra les Labels Tkinter correspondant aux cases
# Chaque élément sera remplacé plus tard par un widget Label
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]


# Fonction qui compresse et fusionne 4 cases comme dans le jeu 2048
# Les valeurs sont traitées de gauche à droite
def pack4(a, b, c, d):
    nmove=0
    # Si la troisième case est vide, on décale la quatrième
    if c == 0:
        c = d
        d = 0
    nmove += 1
    # Si la deuxième case est vide, on décale les suivantes
    if b == 0:
        b = c
        c = d
        d = 0
    nmove += 1

    # Si la première case est vide, on décale toutes les valeurs vers la gauche
    if a == 0:
        a = b
        b = c
        c = d
        d = 0
    nmove += 1
    # Fusion des deux premières cases si elles sont identiques
    if a == b:
        a = a * 2
        b = c
        c = d
        d = 0
    nmove += 1
    # Fusion des deuxième et troisième cases si identiques
    if b == c:
        b = b * 2
        c = d
        d = 0
    nmove += 1
    # Fusion des troisième et quatrième cases si identiques
    if c == d:
        c = c * 2
        d = 0
    nmove += 1
    # Retourne les nouvelles valeurs après compression et fusion
    return a, b, c, d,nmove



# Fonction exécutée lorsque le joueur appuie sur la touche "bas"
# Les colonnes sont traitées du bas vers le haut
def down():
    tot_move = 0
    for col in range(4):
        (game[3][col], game[2][col], game[1][col], game[0][col],nmove) = pack4(game[3][col], game[2][col], game[1][col],game[0][col])

        tot_move += nmove
    return tot_move

# Fonction exécutée lorsque le joueur appuie sur la touche "haut"
# Les colonnes sont traitées du haut vers le bas
def up():
    for col in range(4):
        (game[0][col], game[1][col], game[2][col], game[3][col],nmove) = pack4(game[0][col], game[1][col], game[2][col],game[3][col])



# Fonction exécutée lorsque le joueur appuie sur la touche "gauche"
# Chaque ligne est compressée vers la gauche
def left():
    for line in range(4):
        (game[line][0], game[line][1], game[line][2], game[line][3],nmove) = pack4(game[line][0], game[line][1], game[line][2],game[line][3])



# Fonction exécutée lorsque le joueur appuie sur la touche "droite"
# Chaque ligne est compressée vers la droite
def right():
    for line in range(4):
        (game[line][3], game[line][2], game[line][1], game[line][0],nmove) = pack4(game[line][3], game[line][2],game[line][1], game[line][0])

