from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("圈圈叉叉")

clicked = True
count = 0

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkifwon():
    global winner
    winner = False

    if (b1["text"] == b2["text"] == b3["text" != " "]) or (b4["text"] == b5["text"] == b6["text"] != " ") or (b7["text"] == b8["text"] == b9["text"] != " ") or (b1["text"] == b4["text"] == b7["text"] != " ") or (b2["text"] == b5["text"] == b8["text"] != " ") or (b3["text"] == b6["text"] == b9["text"] != " ") or (b1["text"] == b5["text"] == b9["text"] != " ") or (b3["text"] == b5["text"] == b7["text"] != " "):
        winner = True
        messagebox.showinfo(message="你贏了")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("平手")
        disable_all_buttons()


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        
    else:
        messagebox.showinfo(message="這裡不能擺子")

    if count > 1:
        checkifwon()


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked
    clicked = True
    count = 0

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="gray", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)

reset()

root.mainloop()