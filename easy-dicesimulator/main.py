import tkinter                          ##Imported to use Tkinter and make GUI applications.
from PILasOPENCV import Image          ##Imported from PIL, i.e. Python Imaging Library. We use it to perform operations involving images in our UI.
import random                           ##Imported to generate random numbers.

# Building a toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('TS2- Roll the Dice')

# Adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text="Hello There!", fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
l1.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = Image.show(random.choice(dice))

# construct a label widget for image
label1 = tkinter.Label(root, image=image1)
label1.image = image1

# packing a widget in the parent widget 
label1.pack( expand=True)

# function activated by button
def rolling_dice():
    image1 = Image.show(random.choice(dice))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()
