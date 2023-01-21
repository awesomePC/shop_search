import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import * 
from tkinter import TclError, ttk
from tkinter.messagebox import showwarning, askokcancel, WARNING


 #global main window
global window
window = tk.Tk()
window.title('Any Scrap')
#window width, height define
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()  
        
window.geometry("%dx%d" % (width, height))
window.configure(bg='gray')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)
window.columnconfigure(7, weight=1)
window.columnconfigure(8, weight=1)
window.columnconfigure(9, weight=1)
window.columnconfigure(10, weight=1)
window.columnconfigure(11, weight=1)
window.columnconfigure(12, weight=1)
window.columnconfigure(13, weight=1)
window.columnconfigure(14, weight=1)
window.columnconfigure(15, weight=1)



window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)
window.rowconfigure(9, weight=1)

#Title label
# title = tk.Label(window, text='Shop system API',bg='#181515', fg='#FFF', font=50)
# title.config(font=('Helvetica bold',60))
# title.grid(column=4, row=0, columnspan=6, padx=0, sticky=tk.W)

#secret label
secret = tk.Label(window, text='key',bg='#181515', fg='#FFF', font=50)
secret.config(font=('Helvetica bold',30))
secret.grid(column=4, row=2, columnspan=3, padx=40, sticky=tk.W)

#secret input
secret_input =tk.Entry(window, width=10)
secret_input.config(font=('Helvetica bold',30))
secret_input.grid(column=6, row=2, columnspan=3, padx=0, sticky=tk.W)

#key label
key = tk.Label(window, text='secret',bg='#181515', fg='#FFF', font=50)
key.config(font=('Helvetica bold',30))
key.grid(column=4, row=3, columnspan=3, padx=40, sticky=tk.W)

#secret input
key_input =tk.Entry(window, width=10)
key_input.config(font=('Helvetica bold',30))
key_input.grid(column=6, row=3, columnspan=3, padx=0, sticky=tk.W)

#buttons
buttons = []
for i in range(3):
    for j in range(16):
        button = tk.Button(window, text = f"dist_{i*16+j}", command="onclick")
        button.config(font=('Helvetica bold',20))
        button.grid(column=j, row=4+i, columnspan=1, padx=0, sticky=tk.W)

        buttons.append(button)

def onclick():
    pass
# entry= Entry(win, width= 40)
# entry.focus_set()
# entry.pack()
btn_start = tk.Button(window, text = f"start", bg='#181515', fg='#FFF', command="")
btn_start.config(font=('Helvetica bold',30))
btn_start.grid(column=13, row=8, columnspan=3, padx=0, sticky=tk.W)
#Create a Button to validate Entry Widget
# ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

#start mainwindow
window.mainloop()