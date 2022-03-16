Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> root = Tk()
>>> root.geometry("300x100")
''
>>> label1 = Label(root, text="혼공 SQL은")
>>> label2 = Label(root, text="쉽습니다.", font=("궁서체", 30), bg="blue", fg="yellow")
>>> label1.pack()
>>> label2.pack()
>>> root.mainloop()
