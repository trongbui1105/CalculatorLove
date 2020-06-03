// APP
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from collections import Counter


def main():
	root = Tk()
	root.geometry('350x200')
	root.title('Calculator Love Game')
	root.configure(bg = 'pink')


	image = Image.open("pic.jpg")
	image = image.resize((350, 250), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)
	label = Label(image=photo)
	label.pack()
	btn = Button(root, text='Play', highlightbackground="pink", fg = 'blue', height=1, width=4, command=clicked)
	btn.config(font=('Arial', 30))
	btn.place(x=220, y=60)	

	root.mainloop()



def clicked():

	root1 = Tk()
	root1.geometry('400x250')
	root1.title('Calculator Love Game')
	root1.configure(bg='pink')

	lbl = Label(root1, text = "Let's Play", bg = 'pink', fg = 'blue')
	lbl.config(font=('Menlo', 48))
	lbl.pack()

	yourlabel = Label(root1, text = "Your Name", bg = 'pink', fg = 'black')
	yourlabel.config(font=('Arial', 16))
	yourlabel.place(x=35,y=71)

	loverlabel = Label(root1, text = "Your Lover's Name", bg = 'pink', fg = 'black')
	loverlabel.config(font=('Arial', 16))
	loverlabel.place(x=15,y=151)

	
	yourname_entry = Entry(root1, width = 25)
	yourname_entry.place(x=150, y=70)

	
	lovername_entry = Entry(root1, width = 25)
	lovername_entry.place(x=150, y=150)


	def check():
		name1 = yourname_entry.get()
		name2 = lovername_entry.get()
		name1 = name1.replace(" ", "").lower()
		name2 = name2.replace(" ", "").lower()
		s1 = Counter(name1)
		s2 = Counter(name2)
		s = s1 & s2
		count = 0
		for value in s:
			count += s[value]
		return count


	def cal():
		cnt = check()
		name1 = yourname_entry.get()
		name2 = lovername_entry.get()
		name1 = name1.replace(" ", "").lower()
		name2 = name2.replace(" ", "").lower()
		if(len(name1) == 0 or len(name2) == 0):
			info = "You do not input into the blank. Try again!"
			messagebox.showwarning("Warning", info)
		else:
			per = 100 / (len(name1) + len(name2))
			res = 2 * cnt * per
			text = "The chances of finding true love together: " + str(round(res, 2)) + "%"
			messagebox.showinfo('Congratulations', text)

		yourname_entry.delete(0, END)
		lovername_entry.delete(0, END)

	newbtn = Button(root1, text = 'Check', highlightbackground='pink', fg='blue', command=cal, height=1,width = 5)
	newbtn.config(font=('Arial', 22))
	newbtn.place(x = 175, y = 200)
	root1.mainloop()
	


main()

