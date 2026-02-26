# Test Ma20
# Maxime Ernst
# 05.02.2026
# dynamic creation of labels (pack)

from tkinter import *      # Importation de Tkinter pour créer l'interface graphique
from core import *         # Importation du module core (contient probablement le dictionnaire colors)

# Liste 2 dimensions avec les données du jeu (grille 2048)
"""
game= [[0, 0, 2,0],
        [0,2, 0,0],
        [0, 0, 0,0],
        [0, 0, 0,0]]
"""
# Grille de test remplie avec des valeurs
game= [[2, 4, 8,16],
        [32,64, 128,256],
        [512, 1024, 2048,4096],
        [8192,0,0,0]]

# Liste 2 dimensions vide (contiendra les objets Label plus tard)
labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]

dx=10 # distance horizontale entre les labels
dy=10 # distance verticale entre les labels

# Création de la fenêtre principale
win = Tk()
win.geometry("800x680")          # Taille de la fenêtre
win.title('2048')                # Titre de la fenêtre
win.configure(background='#808080')  # Couleur de fond

# Frame pour les boutons et le titre
frm_btn = Frame(win,background='#808080')
frm_btn.pack(fill=BOTH,anchor=NW)

# Label score
lbl_score = Label(frm_btn,text="score",bg='#DBD4CA',height=3,width=15)
lbl_score.pack(side=LEFT)
lbl_score.pack(side=LEFT,padx=40)  # Ajout d’un espace horizontal

# Label meilleur score
lbl_Bestscore = Label(frm_btn,text="Meilleur score",bg='#DBD4CA',height=3,width=15)
lbl_Bestscore.pack(side=LEFT,padx=0)

# Titre du jeu
lbl_title=Label(frm_btn,bg='#808080',text="2048", height=2,font=("Arial", 35,))
lbl_title.pack(side=LEFT,padx=50)

# Bouton quitter
btn_quitter = Button(frm_btn,background='#DBD4CA', text="Quitter", command=win.quit)
btn_quitter.pack(side=LEFT,padx=40)

# Fonction pour afficher la grille et remplacer les 0 par vide
def display():
    for line in range(len(game)):              # Parcours des lignes
        for col in range(len(game[line])):    # Parcours des colonnes
            if game[line][col] > 0:           # Si la valeur est différente de 0
                labels[line][col].config(
                    text=game[line][col],     # Affiche le nombre
                    bg=colors[game[line][col]]  # Change la couleur selon la valeur
                )
            else:
                labels[line][col].config(
                    text="",                  # Affiche vide si 0
                    bg=colors[game[line][col]]
                )

# Création dynamique de la grille graphique
for line in range(len(game)):
    frm=Frame(win,background='#DBD4CA')  # Frame temporaire pour chaque ligne
    frm.pack()

    for col in range(len(game[line])):
        # Création du label (case du jeu) sans placement
        labels[line][col] = Label(
            frm,
            text=game[line][col],                 # Valeur initiale
            width=6,
            height=3,
            borderwidth=1,
            relief="solid",
            font=("Arial", 15),
            bg=colors[game[line][col]]            # Couleur selon la valeur
        )

        # Placement du label dans la fenêtre (alignement horizontal)
        labels[line][col].pack(side=LEFT, padx=dx, pady=dy)

# Lancement de la boucle principale (affichage de la fenêtre)
win.mainloop()