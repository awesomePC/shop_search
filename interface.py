import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import * 
from tkinter import TclError, ttk
from tkinter.messagebox import showwarning, askokcancel, WARNING
import json

 #global main window
 #pyjsonview install and change

def startScreen():
    
    global window
    window = tk.Tk()
    window.title('Any Scrap')
    #window width, height define
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight()  
            
    window.geometry("%dx%d" % (width, height))
    window.configure(bg='gray')

      #window gird column, row define 
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)


    # global maincanvas
    maincanvas = tk.Frame(window,  width= window.winfo_screenwidth(), height= window.winfo_screenheight(), bg="gray")
    maincanvas.grid(column=0, row=0, columnspan=2,  sticky='nsew')

    maincanvas.columnconfigure(0, weight=1)
    maincanvas.columnconfigure(1, weight=1)
    maincanvas.columnconfigure(2, weight=1)
    maincanvas.columnconfigure(3, weight=1)
    maincanvas.columnconfigure(4, weight=1)
    maincanvas.columnconfigure(5, weight=1)
    maincanvas.columnconfigure(6, weight=1)
    maincanvas.columnconfigure(7, weight=1)
    maincanvas.columnconfigure(8, weight=1)
    maincanvas.columnconfigure(9, weight=1)
    maincanvas.columnconfigure(10, weight=1)
    maincanvas.columnconfigure(11, weight=1)
    maincanvas.columnconfigure(12, weight=1)
    maincanvas.columnconfigure(13, weight=1)
    maincanvas.columnconfigure(14, weight=1)
    maincanvas.columnconfigure(15, weight=1)



    maincanvas.rowconfigure(0, weight=1)
    maincanvas.rowconfigure(1, weight=1)
    maincanvas.rowconfigure(2, weight=1)
    maincanvas.rowconfigure(3, weight=1)
    maincanvas.rowconfigure(4, weight=1)
    maincanvas.rowconfigure(5, weight=1)
    maincanvas.rowconfigure(6, weight=1)
    maincanvas.rowconfigure(7, weight=1)
    maincanvas.rowconfigure(8, weight=1)
    maincanvas.rowconfigure(9, weight=1)

    #Title label
    # title = tk.Label(window, text='Shop system API',bg='#181515', fg='#FFF', font=50)
    # title.config(font=('Helvetica bold',60))
    # title.grid(column=4, row=0, columnspan=6, padx=0, sticky=tk.W)

    #secret label
    secret = tk.Label(maincanvas, text='key',bg='#181515', fg='#FFF', font=50)
    secret.config(font=('Helvetica bold',30))
    secret.grid(column=4, row=2, columnspan=3, padx=40, sticky=tk.W)

    #secret input
    global secret_input
    secret_input =tk.Entry(maincanvas, width=10)
    secret_input.config(font=('Helvetica bold',30))
    secret_input.grid(column=6, row=2, columnspan=3, padx=0, sticky=tk.W)

    #key label
    key = tk.Label(maincanvas, text='secret',bg='#181515', fg='#FFF', font=50)
    key.config(font=('Helvetica bold',30))
    key.grid(column=4, row=3, columnspan=3, padx=40, sticky=tk.W)

    #secret input
    global key_input
    key_input =tk.Entry(maincanvas, width=10)
    key_input.config(font=('Helvetica bold',30))
    key_input.grid(column=6, row=3, columnspan=3, padx=0, sticky=tk.W)

    #variable to show selected button
    select_button = 0

    #buttons
    global buttons
    buttons = []
    for i in range(3):
        for j in range(16):
            id = i*16+j
            button = tk.Button(maincanvas, text = f"dist_{i*16+j}", command=lambda: onclick(id))
            button.config(font=('Helvetica bold',20))
            button.grid(column=j, row=4+i, columnspan=1, padx=0, sticky=tk.W)
            
            buttons.append(button)

    # entry= Entry(win, width= 40)
    # entry.focus_set()
    # entry.pack()
    btn_start = tk.Button(maincanvas, text = f"start", bg='#181515', fg='#FFF', command= lambda:start())
    btn_start.config(font=('Helvetica bold',30))
    btn_start.grid(column=13, row=8, columnspan=3, padx=0, sticky=tk.W)
    #Create a Button to validate Entry Widget
    # ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)


    #start mainwindow
    window.mainloop()

def onclick(id):
    print(id)
    global buttons
    global select_button
    if select_button != 0:
        buttons[select_button].config(font=('Helvetica bold',20), fg="black")
    select_button = id
    buttons[select_button].config(font=('Helvetica bold',20), fg="red")

def mainScreen():
    global window 
    for widgets in window.winfo_children():
      widgets.destroy()

    # window.geometry("%dx%d" % (width, height))
    window.configure(bg='gray')

    #  #secret label
    # # secret = tk.Label(window, text='key',bg='#181515', fg='#FFF', font=50)
    # # secret.config(font=('Helvetica bold',30))
    # # secret.grid(column=4, row=2, columnspan=3, padx=40, sticky=tk.W)

    #global right frame
    global side_frame
    side_frame = tk.Frame(window, width=window.winfo_screenwidth()/2, height=window.winfo_screenheight(), bg="gray")
    side_frame.grid(column=0, row=0, columnspan=1,  sticky='nsew')
    # define grid columns
    side_frame.columnconfigure(0, weight=1)
    side_frame.columnconfigure(1, weight=1)
    # define grid rows
    side_frame.rowconfigure(0, weight=1)
    side_frame.rowconfigure(1, weight=1)
    side_frame.rowconfigure(2, weight=4)
    side_frame.rowconfigure(3, weight=1)
    side_frame.rowconfigure(4, weight=1)

    global play
    play = tk.Label(side_frame, text='PLAY', bg='#181515', fg='orange')
    play.config(font=('Helvetica bold',30))
    play.grid(column=0, row=0, padx= 10, sticky=tk.E)
    
    btn_start = tk.Button(side_frame, text = f"start", bg='#181515', fg='#FFF', command= lambda:change_json())
    btn_start.config(font=('Helvetica bold',30))
    btn_start.grid(column=13, row=8, columnspan=3, padx=0, sticky=tk.W)


    # data = {'name': "John", 'age': 31, 'city': "New York"}
    # text = json.dumps(data, indent=2)
    # with open("./taobao_json/shop_id=57301367/page_1/page.json") as f:
    #     json_obj = json.load(f)
    # json_obj = json.dumps(json_obj, indent=2)
    # # root = tk.Tk()

    # lbl = tk.Label(side_frame, text=json_obj, font="Times32", justify='left')
    # lbl.grid(column=0, row=1, columnspan=3, padx= 10, sticky=tk.E)

    # #global right frame
    # global main_frame
    # main_frame = tk.Frame(window, width=window.winfo_screenwidth()/2, height=window.winfo_screenheight(), bg="#f5f2eb")
    # main_frame.grid(column=1, row=0, columnspan=1,  sticky='nsew')
  

    

    # # define grid columns
    # main_frame.columnconfigure(0, weight=1)
    # main_frame.columnconfigure(1, weight=1)
    # # define grid rows
    # main_frame.rowconfigure(0, weight=1)
    # main_frame.rowconfigure(1, weight=1)
    # main_frame.rowconfigure(2, weight=4)
    # main_frame.rowconfigure(3, weight=1)
    # main_frame.rowconfigure(4, weight=1)

    # import pyjsonviewer
    # pyjsonviewer.view_data(json_file="../taobao_json/page_1/page.json")

    import pyjsonviewer
    global app
    app = pyjsonviewer.JSONTreeFrame(window, json_path="./taobao_json/shop_id=57301367/page_1/page.json", initial_dir="shop_python")

    # app = JSONTreeFrame(main_frame, json_path="../")

    # # when
    children = app.get_all_children(app.tree)
    print([app.tree.item(item_id, 'text') for item_id in children])
    app.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
    

    app.init_search_box()

    

    # pass

def change_json():

    global app
    app.set_table_data_from_json_path("./taobao_json/shop_id=57301367/page_2/page.json")

def start():
    if not secret_input.get() or not key_input.get():
        showwarning(title='Warning', message='Please fill key and secret.')
    else:
        mainScreen()

startScreen()

# import pyjsonviewer
# pyjsonviewer.JSONTreeFrame(root, json_path="./taobao_json/shop_id=57301367/page_1/page.json", initial_dir="shop_python")

# pyjsonviewer.view_data(json_file="./taobao_json/shop_id=57301367/page_1/page.json")