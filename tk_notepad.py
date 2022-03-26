# creating a notepad using python
from tkinter import *
import tkinter.messagebox as tm
import tkinter.filedialog as tf
import os as o

def new1():
    global file
    root.title("Untitled.txt")
    file = None
    a.delete(1.0, END)       # 1.0-> line 1, 0th character, upto the end
def open1():
    global file
    try:
        file = tf.askopenfilename(filetypes=[("All Files", "*.*")])
        if file == "":
            file = None
        else:
            root.title(o.path.basename(file)+"-notepad**")     # changing the title of the window
            a.delete(1.0, END)
            f = open(file, 'r')
            a.insert(1.0, f.read())
            f.close()
    except:
        tm.showinfo("Error", "File with .txt is allowed.")
def save1():
    global file
    try:
        if file is None:
            file = tf.asksaveasfilename(initialfile='file.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*")])
            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(a.get(1.0, END))
                f.close()
                root.title(o.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            f = open(file, "w")
            f.write(a.get(1.0, END))
            f.close()
    except:
        tm.showinfo("Error", "Please enter an appropriate extension")
def exit1():
    root.destroy()
def cut1():
    a.event_generate(("<<Cut>>"))
def copy1():
    a.event_generate(("<<Copy>>"))
def paste1():
    a.event_generate(("<<Paste>>"))
def help1():
    tm.showinfo("About", "This is a note taking software V 1.0.0")

root = Tk()
root.geometry("344x355")
root.title("Notepad**")
a = Text(root, font="aparajita 13")
file = None
a.pack(expand=True, fill=BOTH)

menu_b = Menu(root)

b = Menu(menu_b, tearoff=0)
b.add_command(label="New", command=new1)
b.add_command(label="Open", command=open1)
b.add_command(label="Save", command=save1)
b.add_separator()
b.add_command(label="Exit", command=exit1)
menu_b.add_cascade(label="File", menu=b)
root.config(menu=menu_b)

c = Menu(menu_b, tearoff=0)
c.add_command(label="Cut", command=cut1)
c.add_command(label="Copy", command=copy1)
c.add_command(label="Paste", command=paste1)
menu_b.add_cascade(label="Edit", menu=c)
root.config(menu=menu_b)

d = Menu(menu_b, tearoff=0)
d.add_command(label="About...", command=help1)
menu_b.add_cascade(label="Help", menu=d)
root.config(menu=menu_b)

scrollbar = Scrollbar(a)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=a.yview)
a.config(yscrollcommand=scrollbar.set)

root.mainloop()
