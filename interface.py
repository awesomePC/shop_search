import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import * 
from tkinter import TclError, ttk
from tkinter.messagebox import showwarning, askokcancel, WARNING
import json

 #global main window
 #pyjsonview install and change
# https://codingdeekshi.com/python-3-tkinter-pagination-project-to-fetch-data-from-rest-api-and-paginate-it-in-table-gui-desktop-app/


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
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)


    # global maincanvas
    maincanvas = tk.Frame(window,  width= window.winfo_screenwidth(), height= window.winfo_screenheight(), bg="gray")
    maincanvas.grid(column=0, row=0, columnspan=3,  sticky='nsew')

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

def mainScreen(pagenum):
    
    global window, page
    page = pagenum
    for widgets in window.winfo_children():
      widgets.destroy()

    # window.geometry("%dx%d" % (width, height))
    window.configure(bg='gray')

    #global right frame
    global side_frame
    side_frame = tk.Frame(window, width=window.winfo_screenwidth()/2, height=window.winfo_screenheight(), bg="gray")
    side_frame.grid(column=0, row=0, columnspan=1,  sticky='nsew')
    # define grid columns
    side_frame.columnconfigure(0, weight=1)
    side_frame.columnconfigure(1, weight=1)
    side_frame.columnconfigure(2, weight=1)
    # define grid rows
    side_frame.rowconfigure(0, weight=1)
    side_frame.rowconfigure(1, weight=1)
    side_frame.rowconfigure(2, weight=1)
    side_frame.rowconfigure(3, weight=1)
    side_frame.rowconfigure(4, weight=1)

    global item_frame
    item_frame = tk.Frame(side_frame, width=window.winfo_screenwidth()/3, height=window.winfo_screenheight()*2/3, bg="gray")
    item_frame.grid(column=0, row=1, columnspan=3,  sticky='nsew')

     # define grid columns
    item_frame.columnconfigure(0, weight=1)
    item_frame.columnconfigure(1, weight=1)
    item_frame.columnconfigure(2, weight=1)
    # define grid rows
    item_frame.rowconfigure(0, weight=1)
    item_frame.rowconfigure(1, weight=1)
    item_frame.rowconfigure(2, weight=1)
    item_frame.rowconfigure(3, weight=1)
    item_frame.rowconfigure(4, weight=1)
    item_frame.rowconfigure(5, weight=1)
    item_frame.rowconfigure(6, weight=1)
    item_frame.rowconfigure(7, weight=1)
    item_frame.rowconfigure(8, weight=1)
    item_frame.rowconfigure(9, weight=1)
    item_frame.rowconfigure(10, weight=1)
    item_frame.rowconfigure(11, weight=1)
    item_frame.rowconfigure(12, weight=1)
    item_frame.rowconfigure(11, weight=1)
    item_frame.rowconfigure(12, weight=1)
    item_frame.rowconfigure(13, weight=1)
    item_frame.rowconfigure(14, weight=1)
    item_frame.rowconfigure(15, weight=1)
    item_frame.rowconfigure(16, weight=1)
    item_frame.rowconfigure(17, weight=1)
    item_frame.rowconfigure(18, weight=1)
    item_frame.rowconfigure(19, weight=1)
    item_frame.rowconfigure(20, weight=1)
    item_frame.rowconfigure(21, weight=1)
    item_frame.rowconfigure(22, weight=1)
    item_frame.rowconfigure(23, weight=1)
    item_frame.rowconfigure(24, weight=1)
    item_frame.rowconfigure(25, weight=1)
    item_frame.rowconfigure(26, weight=1)
    item_frame.rowconfigure(27, weight=1)
    item_frame.rowconfigure(28, weight=1)
    item_frame.rowconfigure(29, weight=1)
    item_frame.rowconfigure(30, weight=1)
    item_frame.rowconfigure(31, weight=1)
    item_frame.rowconfigure(32, weight=1)
    item_frame.rowconfigure(33, weight=1)
    item_frame.rowconfigure(34, weight=1)
    
    with open(f"./taobao_json/shop_id=57301367/page_{page}/page.json", encoding='utf-8' ) as f:
        json_obj = json.load(f)
    data = json_obj["items"]["item"]
    items = []
    i = 0
    for row in data:
        title = row["title"]
        num_iid = row["num_iid"]
        item = tk.Button(item_frame, text = f"dist_{title}", command=lambda: change_json(f"./taobao_json/shop_id=57301367/page_{page}/item_detail/{num_iid}/{num_iid}.json"))
        # item.config(font=('Helvetica bold',20))
        item.grid(column=1, row=i, columnspan=1, padx=0, sticky=tk.W)
        
        items.append(item)
        i+=1
    
    # btn_start = tk.Button(side_frame, text = f"start", bg='#181515', fg='#FFF', command= lambda:change_json())
    # btn_start.config(font=('Helvetica bold',30))
    # btn_start.grid(column=13, row=8, columnspan=3, padx=0, sticky=tk.W)

    
    tk.Button(side_frame, text="prev", command=pre_page).grid(row=3, column=0, sticky=tk.E)
    
    entry_text = tk.StringVar()
    entry_text.set(page)
    global page_input
    page_input =tk.Entry(side_frame, width=5, textvariable=entry_text)
    # page_input.config(font=('Helvetica bold',30))
    page_input.grid(column=1, row=3, columnspan=1)
    page_input.bind('<Return>', enterPageInput)
 
    tk.Button(side_frame, text="next", command=next_page).grid(row=3, column=2, sticky=tk.W)
   

    import pyjsonviewer
    global app
    app = pyjsonviewer.JSONTreeFrame(window, json_path="./taobao_json/shop_id=57301367/page_1/page.json", initial_dir="shop_python")

    # app = JSONTreeFrame(main_frame, json_path="../")

    # # when
    children = app.get_all_children(app.tree)
    # print([app.tree.item(item_id, 'text') for item_id in children])
    app.grid(column=1, row=0, columnspan=2,  sticky=(tk.N, tk.S, tk.E, tk.W))
    
    app.init_search_box()

def next_page():
    global page
    page+=1
    mainScreen(page)

def pre_page():
    global page
    page-=1
    mainScreen(page)

def change_json(path):

    global app
    app.set_table_data_from_json_path(path)
    # app.set_table_data_from_json_path("./taobao_json/shop_id=57301367/page_2/page.json")

def enterPageInput(event):
    global page_input
    input_pagenum = int(page_input.get())
   
    mainScreen(input_pagenum)

def start():
    if not secret_input.get() or not key_input.get():
        showwarning(title='Warning', message='Please fill key and secret.')
    else:
        mainScreen(1)
page = 1
min_page = 1
max_page = 1
startScreen()

# import pyjsonviewer
# pyjsonviewer.JSONTreeFrame(root, json_path="./taobao_json/shop_id=57301367/page_1/page.json", initial_dir="shop_python")

# pyjsonviewer.view_data(json_file="./taobao_json/shop_id=57301367/page_1/page.json")