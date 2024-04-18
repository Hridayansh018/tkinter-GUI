from tkinter import *

window = Tk()#instantiate an instance of a window
window.title("DEKH BHAU!")
photo = PhotoImage(file="photu.png")
window.iconphoto(True, photo)

lable = Label(window,
              text="MAI JA RHA HU AB TUM APNA DEKHO!",
              font=('Arial', 40, 'bold'),
              fg='white',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
lable.pack()
window.mainloop()
