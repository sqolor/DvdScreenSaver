from tkinter import Toplevel, Tk, Label, PhotoImage
from PIL import Image
width, height = Image.open("dvd-logo-png-33.png").size
addx = False
addy = False
x = 0
y = 0
def check_and_multiply():
    global addx,addy,x,y,width,height
    if x == window.winfo_screenwidth()-width or x==0:
        addx=not addx
    if y == window.winfo_screenheight()-height or y==0:
        addy = not addy
    if addx:
        x+=1
    else:
        x-=1
    if addy:
        y+=1
    else:
        y-=1

def move_window():
    check_and_multiply()
    window.geometry("+"+str(x)+"+"+str(y))
    window.attributes('-topmost', 'true')
    window.after(3, move_window)

window = Tk()
window.attributes('-alpha',0.0)
window.iconify()
window = Toplevel(window)
window.overrideredirect(1)
photo = PhotoImage(file="dvd-logo-png-33.png")
label = Label(window, image=photo,bg="blue")
window.wm_attributes("-transparentcolor", "blue")
label.pack()
move_window()
window.mainloop()
