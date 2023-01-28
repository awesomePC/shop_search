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
                    global url_list
                    url_list.append(f"{prev}/{filename}")
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


def downloadImage(filepath):
    print("ok")
    print(filepath)
    global download_num, downloaded_num

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

        filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"
        isExist = os.path.exists(filename)

        if isExist is False:
            download_num += 1
            
            count = 0
            while True:
                response = requests.get(pic_url)
                print(pic_url ,response.status_code)
                if response.status_code == 200:
                    
                    downloaded_num += 1
                    
                    os.makedirs(os.path.dirname(filename), exist_ok=True)

                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    break
                count += 1
                time.sleep(1)
                if count == 5:
                    break

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
                filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"
                isExist = os.path.exists(filename)

                if isExist is False:
                    download_num += 1
                    count = 0
                    while True:
                        response = requests.get(item_img)
                        print(item_img ,response.status_code)
                        if response.status_code == 200:
                            # filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"

                            downloaded_num += 1
                            os.makedirs(os.path.dirname(filename), exist_ok=True)

                            with open(filename, 'wb') as f:
                                f.write(response.content)

                            break
                             
                        count += 1
                        time.sleep(1)
                        if count == 5:
                            break
            
                
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
                filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"
                isExist = os.path.exists(filename)

                if isExist is False:
                    download_num += 1
                    count = 0
                    while True:
                        response = requests.get(desc_img)
                        print(desc_img, response.status_code)
                        if response.status_code == 200:
                            # filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"
                            downloaded_num += 1
                            os.makedirs(os.path.dirname(filename), exist_ok=True)

                            with open(filename, 'wb') as f:
                                f.write(response.content)
                            break
                             
                        count += 1
                        time.sleep(1)
                        if count == 5:
                            break
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
                filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"
                isExist = os.path.exists(filename)

                if isExist is False:
                    download_num += 1
                    count = 0
                    while True:
                        response = requests.get(prop_img)
                        print(prop_img ,response.status_code)
                        if response.status_code == 200:
                            downloaded_num += 1
                            # filename = f"images/{dic_01}/{dic_02}/{dic_03}/{dic_04}/{img_filename}"
                            os.makedirs(os.path.dirname(filename), exist_ok=True)

                            with open(filename, 'wb') as f:
                                f.write(response.content)
                            break
                             
                        count += 1
                        time.sleep(1)
                        if count == 5:
                            break

url_list = []
download_num = 0
downloaded_num = 0
readdir("./taobao_json")
print(url_list)
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=16) as executor:
    executor.map(downloadImage, url_list) #urls=[list of url]

print(f"download_num: {download_num}")
print(f"downloaded_num: {downloaded_num}")
# http://img.alicdn.com/imgextra/i4/133668489/O1CN01Cy4UrN2Ca0trldU12_!!133668489-0-lubanu-s.jpg 420



# https://img.alicdn.com/imgextra/i1/133668489/O1CN01bqlhnn2Ca0xOIP14p_!!133668489.jpg 420
# http://img.alicdn.com/imgextra/i4/133668489/O1CN01jkHHpW2Ca10Ph5FoO_!!133668489.jpg 420
# http://img.alicdn.com/imgextra/i2/133668489/O1CN01kfXTyF2Ca0snHHGdo_!!133668489.jpg 420
# http://img.alicdn.com/imgextra/i2/133668489/O1CN012ZObFG2Ca0uYuPi1Q_!!133668489.jpg 420
# https://img.alicdn.com/imgextra/i3/133668489/O1CN01jOkcS32Ca0xH9bD7f_!!133668489.jpg 420
# http://img.alicdn.com/imgextra/i1/133668489/O1CN01fKWd0C2Ca10PZiCO0_!!133668489.jpg 420
# http://img.alicdn.com/imgextra/i2/133668489/O1CN012ZObFG2Ca0uYuPi1Q_!!133668489.jpg 420
# http://img.alicdn.com/imgextra/i2/133668489/O1CN016FObtT2Ca0sppnHV9_!!133668489.jpg 420
# http://img.alicdn.com/imgextra/i1/133668489/O1CN01fKWd0C2Ca10PZiCO0_!!133668489.jpg 420
