import requests
import json
import os
import time
from threading import Thread
 
def readdir(name):
    prev = name
    with os.scandir(name) as i:
        for entry in i:
            if entry.is_file():
                # print(entry.name)
                filename = entry.name
                #check if json file is item detail
                if filename.split(".")[0] != "page" and filename.split(".")[1] == "json":
                    # downloadImage(filename,f"{prev}/{filename}")
                    downloadThread = Thread(target=downloadImage, args=(filename, f"{prev}/{filename}",))
                    downloadThread.isDaemon = True
                    downloadThread.start()
            elif entry.is_dir():
                # print(entry.name)
                readdir(f"{prev}/{entry.name}")

def downloadImage(jsonfile, filepath):
    print("ok")
    print(jsonfile, filepath)

    with open(filepath) as f:
        json_obj = json.load(f)

        # print(json_obj)

    #image download
  
    #--pic_url image
    if json_obj['item']['format_check'] == "fail":
        print("======================fail=========================")
    else:
        pic_url = json_obj['item']['pic_url']
        if 'http' not in pic_url:
            pic_url = f"http:{pic_url}"
        
        urlForDic = pic_url.split("//")[1]
        dic_01 = urlForDic.split("/")[0]
        dic_02 = urlForDic.split("/")[1]
        dic_03 = urlForDic.split("/")[2]
        dic_04 = urlForDic.split("/")[3]
        img_filename = urlForDic.split("/")[4]

        response = requests.get(pic_url)
        if response.status_code == 200:
            filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"

            isExist = os.path.exists(filename)

            if isExist is False:
                os.makedirs(os.path.dirname(filename), exist_ok=True)

                with open(filename, 'wb') as f:
                    f.write(response.content)

        #--items_image
        item_len = len(json_obj['item']['item_imgs']) 
        if item_len > 0:
            for i in range(item_len):
                item_img = json_obj['item']['item_imgs'][i]['url']

                if 'http' not in item_img:
                    item_img = f"http:{item_img}"

                urlForDic = item_img.split("//")[1]
                dic_01 = urlForDic.split("/")[0]
                dic_02 = urlForDic.split("/")[1]
                dic_03 = urlForDic.split("/")[2]
                dic_04 = urlForDic.split("/")[3]
                img_filename = urlForDic.split("/")[4]

                response = requests.get(item_img)
                if response.status_code == 200:
                    filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"

                    isExist = os.path.exists(filename)

                    if isExist is False:
                        os.makedirs(os.path.dirname(filename), exist_ok=True)

                        with open(filename, 'wb') as f:
                            f.write(response.content)
        #--desc_image
        desc_len = len(json_obj['item']['desc_img']) 
        if desc_len > 0:
            for i in range(desc_len):
                desc_img = json_obj['item']['desc_img'][i]

                if 'http' not in desc_img:
                    desc_img = f"http:{desc_img}"
                
                urlForDic = desc_img.split("//")[1]
                dic_01 = urlForDic.split("/")[0]
                dic_02 = urlForDic.split("/")[1]
                dic_03 = urlForDic.split("/")[2]
                dic_04 = urlForDic.split("/")[3]
                img_filename = urlForDic.split("/")[4]

                response = requests.get(desc_img)
                if response.status_code == 200:
                    filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"

                    isExist = os.path.exists(filename)

                    if isExist is False:
                        os.makedirs(os.path.dirname(filename), exist_ok=True)

                        with open(filename, 'wb') as f:
                            f.write(response.content)
        #--pros_image
        prop_len = len(json_obj['item']['prop_imgs']['prop_img']) 
        if prop_len > 0:
            for i in range(prop_len):
                prop_img = json_obj['item']['prop_imgs']['prop_img'][i]['url']

                if 'http' not in prop_img:
                    prop_img = f"http:{prop_img}"
                urlForDic = prop_img.split("//")[1]
                dic_01 = urlForDic.split("/")[0]
                dic_02 = urlForDic.split("/")[1]
                dic_03 = urlForDic.split("/")[2]
                dic_04 = urlForDic.split("/")[3]
                img_filename = urlForDic.split("/")[4]

                response = requests.get(prop_img)
                if response.status_code == 200:
                    filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"

                    isExist = os.path.exists(filename)

                    if isExist is False:
                        os.makedirs(os.path.dirname(filename), exist_ok=True)

                        with open(filename, 'wb') as f:
                            f.write(response.content)

readdir("./taobao_json")