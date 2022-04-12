from docx2pdf import convert
from tkinter import *
from tkinter import filedialog

def file_path():
    global x
    global y
    browse_scrn = Toplevel()
    browse_scrn.filename = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('word files', '*.docx'),('all files', '*.*')))
    x = browse_scrn.filename
    String = x
    y = x.replace('.docx', '.pdf')


main = Tk()

Label(main, text='Please select the file').grid(row=0)
Button(main, text='Browse', command = file_path).grid(row=1, sticky=N)


main.mainloop()


convert(x,y)

