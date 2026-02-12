# Test Ma20
# 05.02.2026
# dynamic creation of labels (pack)

from tkinter import *
from core import *

# 2 dimensions list with data
"""
game= [[0, 0, 2,0],
        [0,2, 0,0],
        [0, 0, 0,0],
        [0, 0, 0,0]]
"""
game= [[2, 4, 8,16],
        [32,64, 128,256],
        [512, 1024, 2048,4096],
        [8192,0,0,0]]


# 2 dimensions list (empty, with labels in the future)
labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]




dx=10 # horizontal distance between labels
dy=10 # vertical distance between labels

# Windows creation
win = Tk()
win.geometry("800x680")
win.title('2048')
win.configure(background='#808080')

frm_btn = Frame(win,background='#808080')
frm_btn.pack(fill=BOTH,anchor=NW)

lbl_score = Label(frm_btn,text="score",bg='#DBD4CA',height=3,width=15)
lbl_score.pack(side=LEFT)
lbl_score.pack(side=LEFT,padx=40)


lbl_Bestscore = Label(frm_btn,text="Meilleur score",bg='#DBD4CA',height=3,width=15)
lbl_Bestscore.pack(side=LEFT,padx=0)

# Title
lbl_title=Label(frm_btn,bg='#808080',text="2048", height=2,font=("Arial", 35,))
lbl_title.pack(side=LEFT,padx=50)

btn_quitter = Button(frm_btn,background='#DBD4CA', text="Quitter", command=win.quit)
btn_quitter.pack(side=LEFT,padx=40)
#display the grid and change the 0 to nothing
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col] > 0:
                labels[line][col].config(text=game[line][col], bg=colors[game[line][col]])
            else:
                labels[line][col].config(text="", bg=colors[game[line][col]])

for line in range(len(game)):
    frm=Frame(win,background='#DBD4CA') # temporary frame
    frm.pack()

    for col in range(len(game[line])):
        # creation without placement
        labels[line][col] = Label (frm,text =game[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15), bg=colors[game[line][col]])
        # label positionning in the windows
        labels[line][col].pack (side=LEFT, padx=dx,pady=dy)







