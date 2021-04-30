from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
      
root = Tk()
root.geometry("1000x1500")
#menu

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='START')

filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

#Logo
my_img=ImageTk.PhotoImage(Image.open("logo.png"))
my_label=Label(image=my_img)


#Button
def Exiting():
   messagebox.showinfo( "Camera Mouse", "Thanks for Visiting! ")
   exit()
###main Function
def main():
   messagebox.showinfo( "Starting.....", "Program will Start")

B = Button(root, text ="Exit", command = Exiting)
B.pack()

B1 = Button(root, text ="Start Program", command = main)
B1.pack()
mainloop()