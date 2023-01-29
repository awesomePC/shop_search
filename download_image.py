import requests
import json
import os
import time
import urllib.request
from threading import Thread


# https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
# https://pythonprogramming.net/urllib-tutorial-python-3/
# python filename from path

def readdir(name):
    prev = name
    with os.scandir(name) as i:
        for entry in i:
            if entry.is_file():
                # print(entry.name)
                filename = entry.name
                #check if json file is item detail
                if filename.split(".")[1] == "json":
                    #global url_list
                    #url_list.append(f"{prev}/{filename}")
                    gatherImageUrlFrom(f"{prev}/{filename}")
                    ###############################normal way================################################################

                    # downloadImage(filename,f"{prev}/{filename}")

                    #############################Thread way================bad for server because it creates huge number of thread.######################################

                    # downloadThread = Thread(target=downloadImage, args=(f"{prev}/{filename}",))
                    # downloadThread.isDaemon = True
                    # downloadThread.start()

                    ###############################final way using thread poll###########################################
            elif entry.is_dir():
                # print(entry.name)
                readdir(f"{prev}/{entry.name}")

def gatherImageUrlFrom(jsonPath):
    #print(jsonPath)
    folder, filename = os.path.split(jsonPath)
    with open(jsonPath) as file:
        json_obj = json.load(file)

    # if '660802266523' in filename:
    #     debugItem = True

    if filename.split(".")[0] == "page":
        if json_obj['items']['page_size'] == 3000:
            print("===Page json load failed===" + jsonPath)
            return
        else:
            #--pic_url image
            for url in json_obj['items']['item']:
                pic_url = url['pic_url']
                addDownloadUrl(pic_url)
            return
    else: #detail item json
        if json_obj['item']['format_check'] == "fail":
            print("===Detail json load failed===" + jsonPath)
            return

        #--pic_url image
        pic_url = json_obj['item']['pic_url']
        addDownloadUrl(pic_url)

        #--items_image
        item_len = len(json_obj['item']['item_imgs']) 
        if item_len > 0:
            for i in range(item_len):
                item_img = json_obj['item']['item_imgs'][i]['url']
                addDownloadUrl(item_img)

        #--desc_image
        desc_len = len(json_obj['item']['desc_img']) 
        if desc_len > 0:
            for i in range(desc_len):
                desc_img = json_obj['item']['desc_img'][i]
                addDownloadUrl(desc_img)

        #--pros_image
        prop_len = len(json_obj['item']['prop_imgs']['prop_img']) 
        if prop_len > 0:
            for i in range(prop_len):
                prop_img = json_obj['item']['prop_imgs']['prop_img'][i]['url']
                addDownloadUrl(prop_img)

def localPathFrom(url):
    urlForDic = url.split("//")[1]
    folder, fn = os.path.split(urlForDic)
    filename = f"images/{folder}/{fn}"
    return filename

def addDownloadUrl(url):
    pic_url = url
    if 'http' not in pic_url:
        pic_url = f"http:{pic_url}"

    filename = localPathFrom(pic_url)
    isExist = os.path.exists(filename)

    if isExist is False:
        global url_list
        url_list.append(pic_url)

def downloadOneImage(image_url):
    print(image_url)
    filename = localPathFrom(image_url)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    path, headers = urllib.request.urlretrieve(image_url, filename)
    #print(headers)    
    #time.sleep(5)

url_list = []
download_num = 0
downloaded_num = 0
readdir("./taobao_json")
print(url_list)

# Adding information about user agent
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=16) as executor:
    #executor.map(downloadImage, url_list) #urls=[list of url]
    executor.map(downloadOneImage, url_list) #urls=[list of url]

print(f"download_num: {download_num}")
print(f"downloaded_num: {downloaded_num}")
