from tkinter import *
root = Tk()
root.title("Happy Face")

canvas = Canvas(
    root,
    width=400,
    height=400,
)
canvas.pack()

canvas.create_oval(30, 80, 200, 250,
                   width=5,
                   fill="yellow", outline="blue")

canvas.create_oval(90, 100, 100, 140, width=5, outline="black", fill="black")

canvas.create_oval(130, 100, 140, 140, width=5, outline="black", fill="black")

canvas.create_arc(75,110, 155,230, start= 180, extent = 180, fill="red")

root.mainloop()