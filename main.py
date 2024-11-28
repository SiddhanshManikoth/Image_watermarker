import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import turtle


window = Tk()
window.title("image-watermarker")
window.geometry("700x400")
window.config(padx=50, pady=50)




placeholder = Image.open("img placeholder.png")
placeholder=placeholder.resize((200,200))
placeholder=ImageTk.PhotoImage(placeholder)



base_img=tk.Label(window)
base_img.grid(row=3,column=1)
base_img.image = placeholder
base_img['image'] = placeholder

mark_img=tk.Label(window)
mark_img.grid(row=3,column=2)
mark_img.image = placeholder
mark_img['image'] = placeholder

final_img=tk.Label(window)
final_img.grid(row=3,column=3)
final_img.image = placeholder
final_img['image'] = placeholder

Orignal_image=Image.open("img placeholder.png")
Orignal_watermark=Image.open("img placeholder.png")
WaterMarked_image=Image.open("img placeholder.png")

def upload_base_img_file():
    f_type=[('JPG files','*.jpg'),('PNG files','*.png')]
    filename=tk.filedialog.askopenfilename(filetypes=f_type)
    global Orignal_image
    Orignal_image=Image.open(filename)
    img=Image.open(filename)
    img=img.resize((200,200))
    img=ImageTk.PhotoImage(img)
    base_img.grid(row=3,column=1)
    base_img.image=img
    base_img['image']=img



def upload_mark_img_file():
    f_type = [('JPG files', '*.jpg'), ('PNG files', '*.png')]
    filename = tk.filedialog.askopenfilename(filetypes=f_type)
    global Orignal_watermark ,Orignal_image
    Orignal_watermark = Image.open(filename)
    img = Image.open(filename)
    img=img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    mark_img.grid(row=3, column=2)
    mark_img.image = img
    mark_img['image'] = img
    watermarker(Orignal_image,Orignal_watermark)

def show_final_img(img):
    size = (200, 200)
    img.thumbnail(size)
    img = ImageTk.PhotoImage(img)
    final_img.image = img
    final_img['image'] = img



def watermarker(main_img,watermark_img):

    global WaterMarked_image
    size = (300, 100)
    watermark_img.thumbnail(size)
    wid, hgt = main_img.size
    water_marker_x = wid - 100
    water_marker_y = hgt - 100
    main_img.paste(watermark_img, (water_marker_x, water_marker_y), watermark_img)
    WaterMarked_image =main_img

    show_final_img(WaterMarked_image)

def save_img():

    top = Toplevel(window)
    top.geometry("200x100")
    name_var = tk.StringVar()
    name_label = tk.Label(top, text='name your watermarked img', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(top, textvariable=name_var, font=('calibre', 10, 'normal'))
    name_label.grid(row=2, column=1)
    name_entry.grid(row=3, column=1)
    def submit():
        name = name_var.get()
        global WaterMarked_image
        extentsion = WaterMarked_image.format
        WaterMarked_image.save(f"Mark-images/{name}.{extentsion}")
        global placeholder , base_img, mark_img , final_img, Orignal_image, Orignal_watermark
        base_img.image = placeholder
        base_img['image'] = placeholder
        mark_img.image = placeholder
        mark_img['image'] = placeholder
        final_img.image = placeholder
        final_img['image'] = placeholder
        Orignal_image = Image.open("img placeholder.png")
        Orignal_watermark = Image.open("img placeholder.png")
        WaterMarked_image = Image.open("img placeholder.png")
        top.destroy()

    sub_btn = tk.Button(top, text='Save', command=submit)
    sub_btn.grid(row=4, column=1)
    top.title("Child Window")
    Label(top, text="name the image file")


title=Label(text="IMAGE WATERMARKER")
title.grid(column=1,row=0)
upload_img_button=Button(text="upload image",command=upload_base_img_file)
upload_img_button.grid(column=1,row=4)
upload_watermark_button=Button(text="upload watermark",command=upload_mark_img_file)
upload_watermark_button.grid(column=2,row=4)
save_watermarked_button=Button(text="save watermarked image",command=save_img)
save_watermarked_button.grid(column=3,row=4)

window.mainloop()
