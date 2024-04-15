from tkinter import*

def move_up(event):
    #label.place(x=label.winfo_x(),y=label.winfo_y()-10)
    canvas.move(pic,0,-10)

def move_down(event):
    # label.place(x=label.winfo_x(),y=label.winfo_y()+10)
    canvas.move(pic,0,10)

def move_left(event):
    #label.place(x=label.winfo_x()-10,y=label.winfo_y())
    canvas.move(pic,-10,0)

def move_right(event):
    #label.place(x=label.winfo_x()+10,y=label.winfo_y())
    canvas.move(pic,10,0)


window = Tk()
window.geometry("700x700")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)


canvas=Canvas(window,width=700,height=700)
canvas.pack()

img = PhotoImage(file="Insta.png")
pic = canvas.create_image(0,0,image=img,anchor=NW)
#label = Label(window, image=img)
#label.place(x=0,y=0)


canvas.pack()

window.mainloop()