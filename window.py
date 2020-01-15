# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2

def save_image():
    path = filedialog.asksaveasfilename()
    print(path)
    cv2.imwrite( path+"-edged.jpg", can )

def show_save_button():
    btn2 = Button(root, text="Salveaza fotografia", command=save_image)
    btn2.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

def select_image():
    # grab a reference to the image panels
    global panelA, panelB, can
    # open a file chooser dialog and allow the user to select an input
	# image
    path = filedialog.askopenfilename()
    # ensure a file path was selected
    if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 50, 100)
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
        image = Image.fromarray(image)
        edged = Image.fromarray(can)
 
		# ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        # if the panels are None, initialize them
        show_save_button()

        if panelA is None or panelB is None:
			# the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
 
			# while the second panel will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)
		# otherwise, update the image panels
        else:
			# update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged
            
# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Selecteaza o fotografie", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")


 
# kick off the GUI
root.mainloop()