import tkinter as tk
from win32api import GetSystemMetrics
from PIL import ImageTk, Image

class Gui:
    # Gui constructor
    def __init__ (self):
        window = tk.Tk(className="random legend")
        window.configure(bg="#B93038")
        
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        window.geometry(str(round(screen_width*0.5)) + "x" + str(round(screen_height*0.7)))
        print(str(round(screen_width*0.5)))
        window.eval('tk::PlaceWindow . center')

        # Image of charecter
        image_main = Image.open("Images\Characters\Wraith.png")
        #image_main = img.resize((50, 50), Image.ANTIALIAS)
        
        test = ImageTk.PhotoImage(image_main)

        label_image = tk.Label(image= test, height=500, width=500 , bg="#B93038").place(x= 230, y= 50)



        window.mainloop()
    
