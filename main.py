# (main) Programme prinicpale qui lance le jeu 2048

from gfx import *   # Importation du module gfx (contient probablement des fonctions graphiques
                    # supplémentaires comme display() ou la configuration visuelle)

# affiche le jeu
block_spawn()
block_spawn()
display()           # Appelle la fonction display() pour mettre à jour l’affichage
                    # de la grille (affiche les valeurs et applique les couleurs)

win.mainloop()      # Lance la boucle principale Tkinter
                    # → permet à la fenêtre de rester ouverte
                    # → attend les actions de l'utilisateur