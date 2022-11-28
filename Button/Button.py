from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Обычная кнопка")
root.geometry("250x200")
btn = ttk.Button(text="Обычная кнопка")
btn.pack(expand=True, ipadx=10, ipady=10,)
root.mainloop()