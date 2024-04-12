from tkinter import*

def button_press(num):
    global eq_text
    eq_text = eq_text+str(num)
    eq_lable.set(eq_text)

def backspace():
    global eq_text
    eq_text = eq_text[:-1]
    eq_lable.set(eq_text)

def clear():
    global eq_text
    eq_text = " "
    eq_lable.set(eq_text)

def equals():
    try:
        global eq_text
        total = str(eval(eq_text))
        eq_lable.set(total)
    except Exception as e:
        eq_lable.set("ERROR")
        print("error aya")

window = Tk()
window.geometry("390x502")
window.title("Calculator")

eq_text = " "
eq_lable = StringVar()

equation = Label(window, textvariable=eq_lable,font=("Helvetica",20),fg="black",bg="white",height=2,width=22)
equation.pack()

frame = Frame(window)
frame.pack()

but_clear = Button(frame, text="AC",command= clear,width = 7, height = 3, font = 35,bg="#675e5e")
but_clear.grid(row=0,column=0)

but_back = Button(frame, text="⌫",command= backspace,width = 7, height = 3, font = 35,bg="#675e5e")
but_back.grid(row=0,column=1)

but_div = Button(frame, text="÷",command=lambda:button_press("/"),width = 7, height = 3, font = 35,bg="#675e5e")
but_div.grid(row=0,column=2)

but_mul = Button(frame, text="×",command=lambda:button_press("*"),width = 7, height = 3, font = 35,bg="#675e5e")
but_mul.grid(row=0,column=3)

but_1 = Button(frame, text="1",command=lambda:button_press(1),width = 7, height = 3, font = 35)
but_1.grid(row=1,column=0)

but_2 = Button(frame, text="2",command=lambda:button_press(2),width = 7, height = 3, font = 35)
but_2.grid(row=1,column=1)

but_3 = Button(frame, text="3",command=lambda:button_press(3),width = 7, height = 3, font = 35)
but_3.grid(row=1,column=2)

but_4 = Button(frame, text="4",command=lambda:button_press(4),width = 7, height = 3, font = 35)
but_4.grid(row=2,column=0)

but_5 = Button(frame, text="5",command=lambda:button_press(5),width = 7, height = 3, font = 35)
but_5.grid(row=2,column=1)

but_6 = Button(frame, text="6",command=lambda:button_press(6),width = 7, height = 3, font = 35)
but_6.grid(row=2,column=2)

but_7 = Button(frame, text="7",command=lambda:button_press(7),width = 7, height = 3, font = 35)
but_7.grid(row=3,column=0)

but_8 = Button(frame, text="8",command=lambda:button_press(8),width = 7, height = 3, font = 35)
but_8.grid(row=3,column=1)

but_9 = Button(frame, text="9",command=lambda:button_press(9),width = 7, height = 3, font = 35)
but_9.grid(row=3,column=2)

decimal = Button(frame, text=".",command=lambda:button_press("."),width = 7, height = 3, font = 35)
decimal.grid(row=4,column=0)

but_0 = Button(frame, text="0",command=lambda:button_press(0),width = 7, height = 3, font = 35)
but_0.grid(row=4,column=1)

plus = Button(frame, text="+",command=lambda:button_press("+"),width = 7, height = 3, font = 35,bg="orange")
plus.grid(row=1,column=3)

minus = Button(frame, text="-",command=lambda:button_press("-"),width = 7, height = 3, font = 35,bg="orange")
minus.grid(row=2,column=3)

equal = Button(frame, text="=",command=equals,width = 15, height = 3, font = 35,bg="orange")
equal.grid(row=4,column=2,columnspan=2)

power = Button(frame, text="^",command=lambda:button_press("**"),width = 7, height = 3, font = 35,bg="orange")
power.grid(row=3,column=3)

window.mainloop()