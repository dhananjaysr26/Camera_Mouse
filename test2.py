from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
top = Tk()

C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "23.jpg")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
img_info = ImageTk.PhotoImage(Image.open("information.png"))
img_label2=Label(image=img_info)
B = Button(top, image=img_info)
B.pack(pady=10,side = "right")
top.mainloop()