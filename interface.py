import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import * 
from tkinter import TclError, ttk
from tkinter.messagebox import showwarning, askokcancel, WARNING
import json
from PIL import Image, ImageTk

 #global main window
 #pyjsonview install and change
# https://codingdeekshi.com/python-3-tkinter-pagination-project-to-fetch-data-from-rest-api-and-paginate-it-in-table-gui-desktop-app/
# https://stackoverflow.com/questions/11723217/python-lambda-doesnt-remember-argument-in-for-loop

def startScreen():
    global window
    window = tk.Tk()
    window.title('Any Scrap')
    #window width, height define
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight()  
    
    # window.geometry("%dx%d" % (width, height))
    window.geometry("%dx%d+0+0" % (width, height-height/15))
    window.configure(bg='gray')

    #window gird column, row define 
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=3)
    window.rowconfigure(1, weight=1)

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

   

    #buttons
    global buttons
    buttons = []
    for i in range(3):
        for j in range(16):
            id = i*16+j
            button = tk.Button(maincanvas, text = f"dist_{i*16+j}", command=lambda id = id: onclick(id))
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
    # print(id)
    global buttons
    global selected_button
    # if selected_button != 0:
    buttons[selected_button].config(font=('Helvetica bold',20), fg="black")
    selected_button = id
    buttons[selected_button].config(font=('Helvetica bold',20), fg="red")

def imageURLAnalyse(url):
    path = ""
    urlForDic = url.split("//")[1]
    dir_1 = urlForDic.split("/")[0]
    dir_2 = urlForDic.split("/")[1]
    dir_3 = urlForDic.split("/")[2]
    dir_4 = urlForDic.split("/")[3]
    filename = urlForDic.split("/")[4]
    path = f"./images/{dir_1}/{dir_2}/{dir_3}/{dir_4}/{filename}"
    return path

def getImageDetailsrc(detail_json):
    global images_detail_path
    images_detail_path = []
    with open(f"{detail_json}", encoding='utf-8' ) as f:
        json_obj = json.load(f)
    pic_url = json_obj['item']['pic_url']
    if 'http' not in pic_url:
            pic_url = f"http:{pic_url}"
    
    images_detail_path.append(imageURLAnalyse(pic_url))

    #--items_image
    item_len = len(json_obj['item']['item_imgs']) 
    if item_len > 0:
        for i in range(item_len):
            item_img = json_obj['item']['item_imgs'][i]['url']

            if 'http' not in item_img:
                item_img = f"http:{item_img}"
            images_detail_path.append(imageURLAnalyse(item_img))

    #--desc_image
    desc_len = len(json_obj['item']['desc_img']) 
    if desc_len > 0:
        for i in range(desc_len):
            desc_img = json_obj['item']['desc_img'][i]

            if 'http' not in desc_img:
                desc_img = f"http:{desc_img}"
            images_detail_path.append(imageURLAnalyse(desc_img))

    #--pros_image
    prop_len = len(json_obj['item']['prop_imgs']['prop_img']) 
    if prop_len > 0:
        for i in range(prop_len):
            prop_img = json_obj['item']['prop_imgs']['prop_img'][i]['url']

            if 'http' not in prop_img:
                prop_img = f"http:{prop_img}"
            images_detail_path.append(imageURLAnalyse(prop_img))


def mainScreen(pagenum):
    
    global window, page
    page = pagenum
    #clear main window content to repalce.
    for widgets in window.winfo_children():
      widgets.destroy()
    window.configure(bg='white')

    #global right frame
    global side_frame
    side_frame = tk.Frame(window, width=window.winfo_screenwidth()/3, height=window.winfo_screenheight(), bg="#dfe3eb")
    # side_frame = tk.Frame(window, width=window.winfo_screenwidth()/3, height=window.winfo_screenheight(), bg="yellow")
    # side_frame.grid(column=0, row=0, columnspan=1, rowspan=2,  sticky=tk.NS)
    side_frame.grid(column=0, row=0, columnspan=1, rowspan=2,  sticky='nswe')
    # define grid columns
    side_frame.columnconfigure(0, weight=1)
    side_frame.columnconfigure(1, weight=1)
    side_frame.columnconfigure(2, weight=1)
    # define grid rows
    side_frame.rowconfigure(0, weight=9)
    side_frame.rowconfigure(1, weight=1)
    # side_frame.rowconfigure(2, weight=1)
    # side_frame.rowconfigure(3, weight=1)
    # side_frame.rowconfigure(4, weight=1)

    #canvas
    # side_canvas = tk.Canvas(side_frame, width=window.winfo_screenwidth()/3, height=window.winfo_screenheight()*3/4, bg="gray")
    side_canvas = tk.Canvas(side_frame, width=window.winfo_screenwidth()/3, height=window.winfo_screenheight()*3/4, bg="red")
    side_canvas.grid(column=0, row=0, columnspan=2,  sticky='nsew')
      # define grid columns
    # side_canvas.columnconfigure(0, weight=1)
    # side_canvas.columnconfigure(1, weight=1)
    # side_canvas.columnconfigure(2, weight=1)
    # # define grid rows
    # side_canvas.rowconfigure(0, weight=1)
    # side_canvas.rowconfigure(1, weight=1)
    # side_canvas.rowconfigure(2, weight=1)
    # side_canvas.rowconfigure(3, weight=1)
    # side_canvas.rowconfigure(4, weight=1)
    #sub frame inside side Frame to display items
    global item_frame
    item_frame = tk.Frame(side_canvas, width=window.winfo_screenwidth()/3, height=window.winfo_screenheight()*3/4, bg="white")
    # item_frame = tk.Frame(side_canvas, width=window.winfo_screenwidth()/3, height=window.winfo_screenheight()*3/4, bg="black")
    # item_frame.grid(column=0, row=1, columnspan=3,  sticky='nsew')

     # define grid columns
    item_frame.columnconfigure(0, weight=1)
    item_frame.columnconfigure(1, weight=1)
    # item_frame.columnconfigure(2, weight=1)
    # item_frame.columnconfigure(3, weight=1)
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
    
    scrollbar = Scrollbar(side_frame, orient="vertical", command=side_canvas.yview)
    
    side_canvas.configure(yscrollcommand=scrollbar.set)
    # make the frame in the canvas_scroll
    side_canvas.create_window((4,4), window=item_frame, anchor="nw", tags="frame")
   
    # bind the frame to the scrollbar
    item_frame.bind("<Configure>", lambda x: side_canvas.configure(scrollregion=side_canvas.bbox("all")))
    window.bind_all("<Down>", lambda x: side_canvas.yview_scroll(1, 'units')) # bind "Down" to scroll down
    window.bind_all("<Up>", lambda x: side_canvas.yview_scroll(-1, 'units')) # bind "Up" to scroll up

    with open(f"./taobao_json/shop_id=57301367/page_{page}/page.json", encoding='utf-8' ) as f:
        json_obj = json.load(f)
    data = json_obj["items"]["item"]
    global items, selected_item, max_page
    max_page = json_obj["items"]["page_count"]
    items = []
    global first_item
    i = 0
    for row in data:
        title = row["title"]
        num_iid = row["num_iid"]
        pic_url = row["pic_url"]
        if i == 0:
            first_item = num_iid
            images_detail_json = f"./taobao_json/shop_id=57301367/page_{page}/item_detail/{num_iid}/{num_iid}.json"
        item = tk.Button(item_frame, text = f"{title}", command=lambda i = i, num_iid = num_iid: change_json(i, f"./taobao_json/shop_id=57301367/page_{page}/item_detail/{num_iid}/{num_iid}.json"))
        #display image

        # Create a photoimage object of the image in the path
        #  "pic_url": "https://img.alicdn.com/imgextra/i3/133668489/O1CN01CNP9RX2Ca0nR2y9J1_!!0-item_pic.jpg",
        url_get = pic_url.split("//")[1]
        # print(url_get)
        dir_1 = url_get.split("/")[0]
        dir_2 = url_get.split("/")[1]
        dir_3 = url_get.split("/")[2]
        dir_4 = url_get.split("/")[3]
        file_name = url_get.split("/")[4]
        try:
            image = Image.open(f"./images/{dir_1}/{dir_2}/{dir_3}/{dir_4}/{file_name}").resize((250, 250))
        except FileNotFoundError:
            image = Image.open(f"./images/img.alicdn.com/imgextra/i2/0/O1CN014bM2ko2Ca0zgUlE47_!!0-item_pic.jpg").resize((250, 250))
        imagesrc = ImageTk.PhotoImage(image)

        label = tk.Label(item_frame, image=imagesrc)
        label.image = imagesrc
        label.grid(column=0, row=i, columnspan=1, padx=0, sticky=tk.E)
        #mouse event to label
        label.bind("<Button-1>", lambda e, i = i, num_iid = num_iid: change_json(i, f"./taobao_json/shop_id=57301367/page_{page}/item_detail/{num_iid}/{num_iid}.json"))
        item.config(font=('Helvetica bold',20))
        if i == selected_item:
            item.config(fg="red")
        item.grid(column=1, row=i, columnspan=1, padx=0, sticky=tk.W)
        
        items.append(item)
        i+=1
    
    #footer to show pre and next buttons.
    footer_frame = tk.Frame(side_frame, bg="white")
    footer_frame.grid(column=1, row=1)
    tk.Button(footer_frame, text="prev", command=pre_page).grid(row=1, column=0, sticky=tk.E)

    entry_text = tk.StringVar()
    entry_text.set(page)
    global page_input
    page_input =tk.Entry(footer_frame, width=5, textvariable=entry_text)
    # page_input.config(font=('Helvetica bold',30))
    page_input.grid(column=1, row=1, columnspan=1)
    page_input.bind('<Return>', enterPageInput)
 
    tk.Button(footer_frame, text="next", command=next_page).grid(row=1, column=2, sticky=tk.W)
    
    #right side Frame to show json tree.
    import pyjsonviewer
    global app
    app = pyjsonviewer.JSONTreeFrame(window, json_path=f"./taobao_json/shop_id=57301367/page_{page}/item_detail/{first_item}/{first_item}.json", initial_dir="shop_python")
    
    # # when
    # children = app.get_all_children(app.tree)
    # print([app.tree.item(item_id, 'text') for item_id in children])
    # app.grid(column=1, row=0, columnspan=2,  sticky=tk.W)
    app.grid(column=1, row=0, columnspan=2, rowspan=1,  sticky=(tk.N, tk.S, tk.E, tk.W))
    # app.init_search_box()
    scrollbar.grid(column=2, row=0, columnspan=1,  sticky='nsw')
    # scrollbar.crollbar.pack( side = RIGHT, fill = Y )


    
    #image canvas on the right bottom
    # get image detail sources
    getImageDetailsrc(f"./taobao_json/shop_id=57301367/page_{page}/item_detail/{first_item}/{first_item}.json")
    global images_detail_path, selected_iamges_datail
    global image_canvas
    image_canvas = tk.Canvas(window,  width= window.winfo_screenwidth()*2/3, height= window.winfo_screenheight()/4, bg="white")
    image_canvas.grid(column=1, row=1, columnspan=2,  sticky='nsew')

    image_canvas.columnconfigure(0, weight=1)
    image_canvas.columnconfigure(1, weight=8)
    image_canvas.columnconfigure(2, weight=1)
    # define grid rows
    image_canvas.rowconfigure(0, weight=1)
    
    tk.Button(image_canvas, text="<", command=preImage).grid(row=0, column=0, sticky=tk.E)
    tk.Button(image_canvas, text=">", command=nextImage).grid(row=0, column=2, sticky=tk.W)
   
    try:
        image = Image.open(images_detail_path[selected_iamges_datail]).resize((750, 450))
    except FileNotFoundError:
        image = Image.open(f"./images/img.alicdn.com/imgextra/i2/0/O1CN014bM2ko2Ca0zgUlE47_!!0-item_pic.jpg").resize((750, 450))
    imagesrc = ImageTk.PhotoImage(image)
    global imglabel
    imglabel = tk.Label(image_canvas, image=imagesrc)
    imglabel.image = imagesrc
    imglabel.grid(column=1, row=0, columnspan=1, padx=0)
    # label.grid(column=1, row=0, columnspan=1, padx=0, sticky='nsew')
    

def next_page():
    global page, selected_item, max_page, selected_iamges_datail
    page+=1
    if page > max_page:
        page = max_page
        showwarning(title='Warning', message=f'This is the last page.')
    else:
        selected_item = 0
        selected_iamges_datail = 0
        mainScreen(page)

def pre_page():
    global page, selected_item, min_page, selected_iamges_datail
    page-=1
    if page < min_page:
        page = min_page
        showwarning(title='Warning', message=f'This is the first page.')
    else:
        selected_item = 0
        selected_iamges_datail = 0
        mainScreen(page)

def nextImage():
    global page, max_page, selected_iamges_datail, images_detail_path
    selected_iamges_datail += 1
    # print(images_detail_path[selected_iamges_datail])
    imgs_len = len(images_detail_path)
    if selected_iamges_datail >= imgs_len:
        selected_iamges_datail = imgs_len-1
        showwarning(title='Warning', message=f'This is the last image.')
 
    else:
        try:
            image = Image.open(images_detail_path[selected_iamges_datail]).resize((750, 450))
        except FileNotFoundError:
            image = Image.open(f"./images/img.alicdn.com/imgextra/i2/0/O1CN014bM2ko2Ca0zgUlE47_!!0-item_pic.jpg").resize((750, 450))
        imagesrc = ImageTk.PhotoImage(image)
        global imglabel, image_canvas
        # imglabel = tk.Label(image_canvas, image=imagesrc)
        imglabel.config(image=imagesrc)
        imglabel.image = imagesrc

def preImage():
    global page, min_page, selected_iamges_datail
    selected_iamges_datail-=1
    if selected_iamges_datail < 0:
        selected_iamges_datail = 0
        showwarning(title='Warning', message=f'This is the first image.')
    else:
        try:
            image = Image.open(images_detail_path[selected_iamges_datail]).resize((750, 450))
        except FileNotFoundError:
            image = Image.open(f"./images/img.alicdn.com/imgextra/i2/0/O1CN014bM2ko2Ca0zgUlE47_!!0-item_pic.jpg").resize((750, 450))
        imagesrc = ImageTk.PhotoImage(image)
        global imglabel, image_canvas
        # imglabel = tk.Label(image_canvas, image=imagesrc)
        imglabel.config(image=imagesrc)
        imglabel.image = imagesrc

def change_json(id,path):
    # print(path)
    global app, items, selected_item
    items[selected_item].config(fg="black")
    items[id].config(fg="red")
    selected_item = id
    app.set_table_data_from_json_path(path)
    # app.set_table_data_from_json_path("./taobao_json/shop_id=57301367/page_2/page.json")

    # change images show
    getImageDetailsrc(path)
    global selected_iamges_datail
    selected_iamges_datail = 0

    try:
        image = Image.open(images_detail_path[selected_iamges_datail]).resize((750, 450))
    except FileNotFoundError:
        image = Image.open(f"./images/img.alicdn.com/imgextra/i2/0/O1CN014bM2ko2Ca0zgUlE47_!!0-item_pic.jpg").resize((750, 450))
    imagesrc = ImageTk.PhotoImage(image)
    global imglabel, image_canvas
    # imglabel = tk.Label(image_canvas, image=imagesrc)
    imglabel.config(image=imagesrc)
    imglabel.image = imagesrc

def enterPageInput(event):
    global page_input, selected_item, min_page, max_page
    selected_item = 0
    input_pagenum = int(page_input.get())
    # print(max_page)
    if input_pagenum > max_page or input_pagenum < min_page:
        showwarning(title='Warning', message=f'Please input value between {min_page} and {max_page}.')
    else:
        mainScreen(input_pagenum)

def start():
    if not secret_input.get() or not key_input.get():
        showwarning(title='Warning', message='Please fill key and secret.')
    else:
        mainScreen(1)
page = 1
min_page = 1
max_page = 1
selected_item = 0
images_detail_json = ""
images_detail_path = []
selected_iamges_datail = 0
#variable to show selected button
selected_button = 0
startScreen()

# import pyjsonviewer
# pyjsonviewer.JSONTreeFrame(root, json_path="./taobao_json/shop_id=57301367/page_1/page.json", initial_dir="shop_python")
# pyjsonviewer.view_data(json_file="./taobao_json/shop_id=57301367/page_1/page.json")