from tkinter import Label, Button, messagebox, Tk
from tkinter.constants import DISABLED, SUNKEN
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename


# Set the root window
root = Tk()
root.title('Image Viewer')
root.resizable(False, False)
root.iconbitmap('photo.ico')

# Load all the images
img1 = ImageTk.PhotoImage(Image.open('Image Viewer/Img_1.jpeg'))
img2 = ImageTk.PhotoImage(Image.open('Image Viewer/Img_2.jpeg'))
img3 = ImageTk.PhotoImage(Image.open('Image Viewer/Img_3.jpeg'))
img4 = ImageTk.PhotoImage(Image.open('Image Viewer/Img_4.jpeg'))
img5 = ImageTk.PhotoImage(Image.open('Image Viewer/Img_5.jpeg'))

image_list = [img1, img2, img3, img4, img5]

my_label = Label(image = img1)
my_label.grid(row=1, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global fwd_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    fwd_button = Button(root, text=' >> ', command= lambda: forward(image_number+1))
    back_button = Button(root, text=' << ', command= lambda: back(image_number-1))

    if image_number == len(image_list):
            fwd_button = Button(root, text=' >> ', state=DISABLED)

    fwd_button.grid(row=2, column=2)
    back_button.grid(row=2, column=0)
    my_label.grid(row=1, column=0, columnspan=3)

    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN)
    status.grid(row=0, column=0, columnspan=3)


def back(image_number):
    global my_label
    global fwd_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    fwd_button = Button(root, text=' >> ', command= lambda: forward(image_number+1))
    back_button = Button(root, text=' << ', command= lambda: back(image_number-1))

    if image_number == 1:
            back_button = Button(root, text=' << ', state=DISABLED)

    fwd_button.grid(row=2, column=2)
    back_button.grid(row=2, column=0)
    my_label.grid(row=1, column=0, columnspan=3)

    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN)
    status.grid(row=0, column=0, columnspan=3)


def upload():
    Tk().withdraw()
    filename = askopenfilename()
    if '.jpeg' not in filename:
        messagebox.showinfo("Error","This was not a picture.")
    else:
        image_list.append(ImageTk.PhotoImage(Image.open(filename)))

upload_button = Button(root, text=' UPLOAD ', command=upload).grid(row=3, column=1)
back_button = Button(root, text=' << ', command=back, state=DISABLED).grid(row=2, column=0)
fwd_button = Button(root, text=' >> ', command= lambda: forward(2)).grid(row=2, column=2)
exit_button = Button(root, text='EXIT', command=exit).grid(row=2, column=1, pady=10)

root.mainloop()


