from tkinter import*
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorhex = color[1]
    window.config(background=colorhex)

window = Tk()

window.title("Select Colour")
window.geometry("500x500")
button = Button(window, text="click me", command=click)
button.pack()
window.mainloop()
