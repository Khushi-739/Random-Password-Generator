from tkinter import *
import random, string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable=title)
label.pack()
title.set("The strength of our password:")


def selection():
    selection = choice.get()


choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection)
R1.pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection)
R2.pack(anchor=CENTER)
R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection)
R3.pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel)
lentitle.pack()

val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13)
spinlenght.pack()


def callback():
    generated_password = passgen()
    lsum.config(text=generated_password)


passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()

lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?"""
advance = poor + average + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


def copy():
    root.clipboard_clear()
    root.clipboard_append(lsum.cget("text"))
    root.update()


passgenButton1 = Button(root, text="Copy Password", bd=5, command=copy, height=2)
passgenButton1.pack()

root.mainloop()
