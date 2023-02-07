# from tkinter import *
# import webview
#
# mycolor = "blue"
#
#
# def paint(event):
#     x1, y1 = (event.x-1), (event.y-1)
#     x2, y2 = (event.x+1), (event.y+1)
#     canvas.create_oval(x1, y1, x2, y2, fill=mycolor, outline=mycolor)
#
#
# def change_color():
#     global mycolor
#     mycolor="red"
#
#
# app = Tk()
# canvas: Canvas = Canvas(app)
# canvas.pack()
# canvas.bind("<B1-Motion>", paint)
# button = Button(app, text="빨강", command=change_color)
# button.pack()
# webview.create_window('view', "http://localhost:3000/paint")
# webview.start()
# app.mainloop()
