import tkinter as tk

# Create the main Tkinter window
window = tk.Tk()

apps = ["Discord", "Whatsapp", "Spotify"]

def order():
    selected_app = apps[x.get()]
    print(f"You Selected {selected_app}!")

# Load images after creating the window

WhatsappImage = tk.PhotoImage(file='Whatsapp.png').subsample(3, 3)
SpotifyImage = tk.PhotoImage(file='Spotify.png').subsample(3, 3)
appImages = [WhatsappImage, SpotifyImage]

x = tk.IntVar()

for index in range(len(appImages)):
    radiobutton = tk.Radiobutton(window,
                                 text=apps[index],
                                 variable=x,
                                 value=index,
                                 padx=25,
                                 font=("Impact", 50),
                                 image=appImages[index],
                                 compound='left',
                                 command=order)
    radiobutton.pack(anchor=tk.W)

window.title('GADBAD H!')
window.mainloop()
