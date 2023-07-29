# PassWord Generatoe Using Tkinter Python

from tkinter import *
import random
import clipboard
import tkinter.messagebox as msgbox


def get_password():
    try:
        a = name.get()
        b = middle_name.get()
        c = last_name.get()
        total_length = int(length.get())
        
        symbol = '!@#$%^&*_+=-~`<>?.'
        digit = '1234567890'
        
        String = a.lower()+b.lower()+c.lower()+a.upper()+b.upper()+c.upper()+symbol+digit
        password = "".join(random.sample(String,total_length))
        return password
    except EOFError as e:
        print("Error,",e)
        
def copy():
    text_to_copy = Gererate()
    print(text_to_copy) 
    clipboard.copy(text_to_copy)
    msgbox.showinfo("Success", "Text copied to clipboard!")
  
def Gererate():
    user = name.get()
    result = get_password()
    Password['text']= '{} Your Generated Password is\n{}'.format(user,result)
    b2 = Button(root, text="Copy", command=copy, width=15)
    b2.place(x=150, y=320)
    return result

if __name__ == "__main__":
    root = Tk()
    root.title("Password Generator")
    root.geometry("420x400+560+210")
    icon = PhotoImage(file='icon.png')
    root.iconphoto(False,icon)
    
    label = Label(root,text="Password Generator",font=('Georiga',25,'bold'))
    label.place(x=50,y=10)
    label1 = Label(root, text="Name :",font=('bold',12))
    label1.place(x=80, y=70)
    label2 = Label(root, text="Middle Name :",font=('bold',12))
    label2.place(x=80, y=100)
    label3 = Label(root, text="Last Name :",font=('bold',12))
    label3.place(x=80, y=130)
    label4 = Label(root,text="Length :",font=('bold',12))
    label4.place(x=80, y=160)
    
    name = StringVar()
    middle_name = StringVar()
    last_name = StringVar()
    length = StringVar()
    
    e1 = Entry(root, textvariable=name)
    e1.place(x=200, y=70)
    e2 = Entry(root, textvariable=middle_name)
    e2.place(x=200, y=100)
    e3 = Entry(root, textvariable=last_name)
    e3.place(x=200, y=130)
    e4 = Entry(root, textvariable=length)
    e4.place(x=200, y=160)
    
    b1 = Button(root, text="Generate", command=Gererate, width=15)
    b1.place(x=150, y=200)
    
    Password= Label(root, text="", font=('Helvetica', 15, 'bold'))
    Password.place(x=25,y=250)
    
    root.mainloop()