from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
	def __init__(self):
		self.q_no=0
		self.display_title()
		self.display_question()
	
		self.opt_selected=IntVar()

		self.opts=self.radio_buttons()
		self.display_options()

		self.buttons()
		

		self.data_size=len(question)

		self.correct=0

	def display_result(self):

		wrong_count = self.data_size - self.correct
		correct = f"Correct Answers: {self.correct}"
		wrong = f"Wrong Answers: {wrong_count}"
		
		score = int(self.correct / self.data_size * 100)
		result = f"In Quiz You Got: {score}%"
		

		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True
	def next_btn(self):

		if self.check_ans(self.q_no):
			

			self.correct += 1

		self.q_no += 1

		if self.q_no==self.data_size:

			self.display_result()
			

			gui.destroy()
		else:
			self.display_question()
			self.display_options()

	def buttons(self):
		

		next_button = Button(gui, text="Next",command=self.next_btn,
		width=6,bg="#4da6ff",fg="white",font=("Times New Roman",20,"bold"),bd=2)
		
		# placing the button on the screen
		next_button.place(x=350,y=380)
		

	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)

		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1

	def display_question(self):

		q_no = Label(gui, text=question[self.q_no], width=53,
		font=( 'Times New Roman' ,16, 'bold' ), anchor= 'w' ,highlightbackground="black", highlightthickness=2)
		

		q_no.place(x=70, y=100)


	def display_title(self):
		
		title = Label(gui, text="QUIZ",
		width=33, bg="#66a3ff",fg="white", font=("Times New Roman", 30, "bold"))
		

		title.place(x=0, y=2)



	def radio_buttons(self):

		q_list = []

		y_pos = 150
		

		while len(q_list) < 4:
			

			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("Times New Roman",15),)

			q_list.append(radio_btn)

			radio_btn.place(x = 100, y = y_pos)

			y_pos += 40
		

		return q_list

def terms_conditions():
    root2 = Tk()
    root2.title("Quiz")
    root2.geometry("800x500+350+160")

    title = Label(root2, text="Term & Conditions",
	width=33, bg="#66a3ff",fg="white", font=("Times New Roman", 30, "bold"))
    title.place(x=0, y=2)
    
    statement1 = Label(root2, text="1) Eligibility: The coding quiz is open to individuals of all ages and programming backgrounds.",
		font=( 'Times New Roman' ,14), anchor= 'w')
    statement1.place(x=25, y=100)
    statement2 = Label(root2, text="2) Time Limit: Participants must finish the quiz within the specified time frame given at the start.",
		font=( 'Times New Roman' ,14), anchor= 'w')
    statement2.place(x=25, y=170)
    statement3 = Label(root2, text="3) Plagiarism: Plagiarism leads to disqualification; participants must submit their original work.",
		font=( 'Times New Roman' ,14), anchor= 'w')
    statement3.place(x=25, y=240)
    statement4 = Label(root2, text="4) Requirements: Participants must ensure their internet connection and computer setup are suitable.",
		font=( 'Times New Roman' ,14), anchor= 'w')
    statement4.place(x=25, y=310)
    statement5 = Label(root2, text="5) Calculation: Quiz organizers' scoring is final, and no appeals or re-evaluations will be considered.",
		font=( 'Times New Roman' ,14), anchor= 'w')
    statement5.place(x=25, y=380)
    close = Button(root2, text="Quit", command=root2.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
    close.place(x=350,y=430)
    root2.mainloop()
    

def register():
    root3 = Tk()
    root3.title("Quiz")
    root3.geometry("800x500+350+160")
    title = Label(root3, text="PYTHON PROGRAMMING QUIZ",
	width=33, bg="#66a3ff",fg="white", font=("Times New Roman", 30, "bold"))
    title.place(x=0, y=2)
    lb = Label(root3,text="REGISITER", width=10,
		font=( 'Times New Roman' ,16, 'bold' ), anchor= 'w' ,highlightbackground="black", highlightthickness=2)
    lb.place(x=330, y=100)
    label1 = Label(root3, text="Name",font=('Times New Roman',15))
    label1.place(x=270, y=170)
    label2 = Label(root3, text="Age",font=('Times New Roman',15))
    label2.place(x=270, y=230)
    
    name = StringVar()
    age = StringVar()
    
    e1 = Entry(root3, textvariable=name,width=28)
    e1.place(x=350, y=170)
    e2 = Entry(root3, textvariable=age,width=28)
    e2.place(x=350, y=230)
    terms = Button(root3, text="Terms", command=terms_conditions,
        width=6,bg="#4da6ff", fg="white",font=("ariel",16," bold"))
    terms.place(x=300,y=290)
    close = Button(root3, text="Start", command=root3.destroy,
        width=6,bg="#4da6ff", fg="white",font=("ariel",16," bold"))
    close.place(x=410,y=290)
    root3.mainloop()


register()
gui = Tk()


gui.geometry("800x500+350+160")


gui.title("Quiz")


with open('data.json') as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])


quiz = Quiz()

terms = Button(gui, text="Terms",command=terms_conditions,width=5,bg="black",fg="white",font=("Arieal",10))
terms.place(x=740,y=13)

gui.mainloop()

