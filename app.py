from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import Action
      
root = Tk()
root.geometry("800x500")
#app background color
app_bg="salmon1"
root.configure(bg=app_bg)
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
img = ImageTk.PhotoImage(Image.open("img/logo.png"))
panel = Label(root, image = img,bg=app_bg)
panel.pack(side = "top")


#Button
def Exiting():
   messagebox.showinfo( "Camera Mouse", "Thanks for Visiting! ")
   exit()
###main Function
def show():
   messagebox.showinfo( "Starting.....", "Program will Start")
   Action.test()
def info():
   messagebox.showinfo( "Information", "How to USE TOUR")

img_satrt = ImageTk.PhotoImage(Image.open("img/start.png"))
img_label=Label(image=img_satrt)
B1 = Button(root,image=img_satrt ,borderwidth=0, command = show,bg=app_bg)
B1.pack(pady=10)

img_exit = ImageTk.PhotoImage(Image.open("img/exit.png"))
img_label1=Label(image=img_exit)
B = Button(root, image=img_exit, command = Exiting,bg=app_bg)
B.pack(pady=10,side = "left")

img_info = ImageTk.PhotoImage(Image.open("img/information.png"))
img_label2=Label(image=img_info)
B = Button(root, image=img_info, command = info,bg=app_bg)
B.pack(pady=10,side = "right")

mainloop()