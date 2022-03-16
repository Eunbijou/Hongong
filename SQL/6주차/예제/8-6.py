Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import messagebox
>>> def clickButton() :
	messagebox.showinfo('버튼 클릭', '버튼을 눌렀습니다..')

	
>>> root = Tk()
>>> root.geometry("200x200")
''
>>> button1 = Button(root, text="여기를 클릭하세요", fg="red", bg="yellow", command=clickButton)
>>> button1.pack(expand=1)
>>> root.mainloop()
>>> 