from tkinter import *

count=0
def click():
    global count
    count+=1
    print("DABA DIYE....!")
    print(count)

window = Tk()#instantiate an instance of a window
window.title("YE BHI DEKH!")
photo = PhotoImage(file="huehue.png")
window.iconphoto(True, photo)
button = Button(window,
              text="MUJHE DABAO!",
              command=click,
              font=('Arial', 40, 'bold'),
              fg='white',
              bg='black',
              bd=10,
#              activeforeground="white",
#              activebackground="black",
             image=photo,
             compound='bottom')
button.pack()
window.mainloop()