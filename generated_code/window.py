from tkinter import *
from PIL import Image, ImageTk

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("750x550")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 550,
    width = 750,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    375.0, 275.0,
    image=background_img)

img0 = Image.open("img0.png")
img0 = ImageTk.PhotoImage(img0)
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 208, y = 106,
    width = 111,
    height = 111)

img1 = Image.open("img0.png")
img1 = ImageTk.PhotoImage(img1)
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 319, y = 106,
    width = 111,
    height = 111)

img2 = Image.open("img0.png")
img2 = ImageTk.PhotoImage(img2)
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 430, y = 106,
    width = 111,
    height = 111)

img3 = Image.open("img0.png")
img3 = ImageTk.PhotoImage(img3)
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 208, y = 217,
    width = 111,
    height = 111)

img4 = Image.open("img0.png")
img4 = ImageTk.PhotoImage(img4)
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 319, y = 217,
    width = 111,
    height = 111)

img5 = Image.open("img0.png")
img5 = ImageTk.PhotoImage(img5)
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 430, y = 217,
    width = 111,
    height = 111)

img6 = Image.open("img0.png")
img6 = ImageTk.PhotoImage(img6)
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 208, y = 328,
    width = 111,
    height = 111)

img7 = Image.open("img0.png")
img7 = ImageTk.PhotoImage(img7)
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 319, y = 328,
    width = 111,
    height = 111)

img8 = Image.open("img0.png")
img8 = ImageTk.PhotoImage(img8)
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 430, y = 326,
    width = 111,
    height = 111)

window.resizable(False, False)
window.mainloop()
