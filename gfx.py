# Test Ma20
# 05.02.2026
# dynamic creation of labels (pack)

from tkinter import *        # Importation de Tkinter pour créer l'interface graphique
from core import *           # Importation des éléments du fichier core (ex: couleurs)

# 2 dimensions list (empty, with labels in the future)
# Matrice vide qui contiendra les Labels Tkinter correspondant aux cases
labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]




dx=10 # horizontal distance between labels (espacement horizontal entre les cases)
dy=10 # vertical distance between labels (espacement vertical entre les cases)

# Windows creation
win = Tk()                           # Création de la fenêtre principale
win.geometry("800x680")              # Taille de la fenêtre
win.title('2048')                    # Titre de la fenêtre
win.configure(background='#808080')  # Couleur de fond

# Frame contenant les boutons et informations en haut
frm_btn = Frame(win,background='#808080')
frm_btn.pack(fill=BOTH,anchor=NW)

# Label affichant le score
lbl_score = Label(frm_btn,text="score",bg='#DBD4CA',height=3,width=15)
lbl_score.pack(side=LEFT)
lbl_score.pack(side=LEFT,padx=40)

# Label affichant le meilleur score
lbl_Bestscore = Label(frm_btn,text="Meilleur score",bg='#DBD4CA',height=3,width=15)
lbl_Bestscore.pack(side=LEFT,padx=0)

# Title
# Label du titre du jeu
lbl_title=Label(frm_btn,bg='#808080',text="2048", height=2,font=("Arial", 35,))
lbl_title.pack(side=LEFT,padx=50)

# Bouton pour quitter l'application
btn_quitter = Button(frm_btn,background='#DBD4CA', text="Quitter", command=win.quit)
btn_quitter.pack(side=LEFT,padx=40)

# display the grid and change the 0 to nothing
# Fonction qui met à jour l'affichage de la grille
def display():
    for line in range(len(game)):                 # Parcours des lignes
        for col in range(len(game[line])):       # Parcours des colonnes
            if game[line][col] > 0:              # Si la valeur est différente de 0
                # On affiche le nombre et on applique la couleur correspondante
                labels[line][col].config(text=game[line][col], bg=colors[game[line][col]])
            else:
                # Si la valeur est 0, on affiche une case vide
                labels[line][col].config(text="", bg=colors[game[line][col]])

# Création dynamique de la grille graphique
for line in range(len(game)):
    frm=Frame(win,background='#DBD4CA') # Frame temporaire pour chaque ligne
    frm.pack()

    for col in range(len(game[line])):
        # Création du Label (case du jeu) sans placement immédiat
        labels[line][col] = Label (frm,
                                   text =game[line][col],
                                   width=6,
                                   height=3,
                                   borderwidth=1,
                                   relief="solid",
                                   font=("Arial", 15),
                                   bg=colors[game[line][col]])
        # Placement du Label dans la fenêtre avec pack()
        labels[line][col].pack (side=LEFT, padx=dx,pady=dy)

# Fonction appelée à chaque fois qu'une touche du clavier est pressée
def key_presssed(event):
    tot_move = 0
    # Récupère le nom de la touche pressée (ex: "Up", "Down", "a", "S", etc.)
    touche = event.keysym

    # Si la touche pressée est la flèche bas ou la touche S/s
    # alors on effectue un déplacement vers le bas
    if touche == "Down" or touche == "s" or touche == "S":
        down()

    # Si la touche pressée est la flèche haut ou la touche W/w
    # alors on effectue un déplacement vers le haut
    if touche == "Up" or touche == "w" or touche == "W":
        up()

    # Si la touche pressée est la flèche gauche ou la touche A/a
    # alors on effectue un déplacement vers la gauche
    if touche == "Left" or touche == "a" or touche == "A":
        left()

    # Si la touche pressée est la flèche droite ou la touche D/d
    # alors on effectue un déplacement vers la droite
    if touche == "Right" or touche == "d" or touche == "D":
        right()

    # Après chaque déplacement, on met à jour l'affichage du jeu
    display()


# Associe l'événement "appui sur une touche du clavier"
# à la fonction key_presssed
# Ainsi, chaque touche pressée déclenche cette fonction
win.bind('<Key>', key_presssed)  # on traite les touches clavier