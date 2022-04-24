import tkinter as tk
from win32api import GetSystemMetrics
from PIL import ImageTk, Image
import random


class Gui:
    # Gui constructor

    def __init__(self):
        # Creation and attributes of the window
        window = tk.Tk(className="random legend")
        window.configure(bg="#B93038")

        # get the size of the users screen and sets the window size to about half of that
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        window.geometry(str(round(screen_width * 0.5)) + "x" + str(round(screen_height * 0.7)))

        # Image label of character
        default_image = ImageTk.PhotoImage(Image.open("Images\Characters\Wraith.png"))
        label_image = tk.Label(image=default_image,
                               height=500,
                               width=500,
                               bg="#B93038")
        label_image.pack(pady=30)

        # Button to change the character
        btn_random = tk.Button(window,
                               text="Change Character",
                               bg="#F97B2E",
                               font="26",
                               pady=4,
                               foreground="white",
                               relief="raised",
                               command=lambda: button_click(label_image))
        btn_random.pack(pady=40)

        window.mainloop()


# Onclick function for the random button
def button_click(label_image):
    random_num = random.randint(1, 20)

    # List with all of the characters
    characters = ["Ash", "Bangalore", "Bloodhound", "Caustic",

                  "Crypto", "Fuse", "Gibraltar", "Horizon",

                  "Lifeline", "Loba", "Mad_Maggie", "Mirage",

                  "Octane", "Pathfinder", "Rampart", "Revenant",

                  "Seer", "Valkyrie", "Wattson", "Wraith"]

    default_image = ImageTk.PhotoImage(
        Image.open("Images\Characters" + "\\" + characters[random_num - 1] + "" + ".png"))
    label_image.configure(image=default_image)
    label_image.PhotoImage = default_image
