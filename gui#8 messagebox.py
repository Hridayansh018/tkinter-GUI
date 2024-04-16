from tkinter import*
from tkinter import messagebox

def click():
     messagebox.showinfo(title="this is a info message box", message="u r human")
     while True:
           messagebox.showerror(title="ERROR!!!", message="ATAK GYA!!!")
     #if messagebox.askokcancel(title="ask ok cancel", message="momoz khaoge.....?"):
     #    print("THIK H BHAU...!")
     #else:
      #   print("YE BHI THIK H BHAU...!")
     # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):
     # print('You retried a thing!')
     # else:
     # print('You canceled a thing! :(')

     # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
     # print('I like cake too :)')
     # else:
     # print('Why do you not like cake? :(')

    #  answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
     # if(answer == 'yes'):
      #     print('I like pie too :)')
      #else:
       #    print('Why do you not like pie? :(')


window = Tk()

button = Button(window,command=click, text="click me")
button.pack()

window.mainloop()