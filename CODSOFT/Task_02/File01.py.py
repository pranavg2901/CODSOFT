from tkinter import *

#function 'click'
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()
    elif text == 'AC':
        scvalue.set("")
        screen.update()
    else: 
        scvalue.set(scvalue.get() + text )
        screen.update()


window = Tk()
window.geometry("500x750+530+15")
window.minsize(500,750)
window.maxsize(500,750)
window.config(bg="gray")
window.title("CALCULATOR")
icon = PhotoImage(file='calicon.png')
window.iconphoto(False,icon)

scvalue = StringVar()
scvalue.set("")
f = Frame(window, padx=20, pady=20)
screen = Entry(f,textvar= scvalue, font = "lucida 50 bold", bg='white')
screen.pack(fill=X, padx=20, pady=15)
f.pack()

o1 = ["7", "8", "9", "+"]
o2 = ["4", "5", "6", "-"]
o3 = ["1", "2", "3", "*"]
o4 = ["0", ".", "=" ,"/"]
o5 = ["AC"]

f = Frame(window, bg="gray", padx=30, pady=10)
for i in o1:
    b = Button(f, text=i, padx=10, pady=10, font = "lucida 25 bold", bg='black', fg='white')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(window, bg="gray", padx=30, pady=10)
for i in o2:
    b = Button(f, text=i, padx=10, pady=10, font = "lucida 25 bold", bg='black', fg='white')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(window, bg="gray", padx=30, pady=10)
for i in o3:
    b = Button(f, text=i, padx=10, pady=10, font = "lucida 25 bold", bg='black', fg='white')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(window, bg="gray", padx=30, pady=10)
for i in o4:
    b = Button(f, text=i, padx=10, pady=10, font = "lucida 25 bold", bg='black', fg='white')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(window, bg="gray", padx=30, pady=10)
for i in o5:
    b = Button(f, text=i, padx=45, pady=10, font = "lucida 25 bold",bg= 'orange', fg='white')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

window.mainloop()