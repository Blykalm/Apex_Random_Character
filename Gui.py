import tkinter as tk
from win32api import GetSystemMetrics
from PIL import ImageTk, Image

class Gui:
    # Gui constructor

    def __init__ (self):
        # Createon and attributes of the window
        window = tk.Tk(className="random legend")
        window.configure(bg="#B93038")
        
        # get the size of the users screen and sets the window size to about half of that
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        window.geometry(str(round(screen_width*0.5)) + "x" + str(round(screen_height*0.7)))

        # Image label of charecter
        default_image = ImageTk.PhotoImage(Image.open("Images\Characters\Wraith.png"))
        label_image = tk.Label(image= default_image, 
                               height=500, 
                               width=500 , 
                               bg="#B93038").pack(pady= 30)

        # Button to change the character
        btn_random = tk.Button(window,
                              text= "Change Character", 
                              bg = "#F97B2E", 
                              font= "26", 
                              pady=4,
                              foreground="white",
                              relief="raised").pack(pady= 40)
    

        window.mainloop()
    
