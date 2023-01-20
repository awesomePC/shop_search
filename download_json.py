
# {
#     "error": "",
#     "reason": "",
#     "error_code": "0000",
#     "cache": 0,
#     "api_info": "today: max:20000 all[=++];expires:2024-01-16",
#     "execution_time": "0.565",
#     "server_time": "Beijing/2023-01-20 04:13:54",
#     "client_ip": "188.43.136.46",
#     "call_args": {
#         "seller_nick": "433655136",
#         "start_price": "4"
#     },
#     "api_type": "taobao",
#     "translate_language": "zh-CN",
#     "translate_engine": "baidu",
#     "server_memory": "5.73MB",
#     "last_id": false
# }







from __future__ import print_function
import requests
import json
import os
import time
from threading import Thread

# hp.tmall.com
# shop_id 57301367
# https://api-gw.onebound.cn/taobao/item_search_shop/?key=t_856 2094008186&&shop_id=57301367&page=1&sort=&&lang=zh-CN&secret=20230114



# Request example url The default request parameters have been URL-encoded
# url = "https://api-gw.onebound.cn/taobao/item_search_shop/?key=t_856 2094008186&&shop_id=433655136&page=1&sort=&&lang=zh-CN&secret=20230114&cache=no"
url = "https://api-gw.onebound.cn/taobao/item_search_shop/?key=t_856 2094008186&&shop_id=57301367&page=1&sort=&&lang=zh-CN&secret=20230114"
headers = {
    "Accept-Encoding": "gzip",
    "Connection": "close"
}

def downloadJson(item, page):
    print("======================================================")
    num_iid = item["num_iid"]
    pic_url = item["pic_url"]
    #image download    ====================
    if 'http' not in pic_url:
        pic_url = f"http:{pic_url}"
    response = requests.get(pic_url)
    # if response.status_code == 200:
    #     print("img")

    #     filename = f"{district}/{shop_id}/page_{page}/item_image/{num_iid}.jpg"
    #     os.makedirs(os.path.dirname(filename), exist_ok=True)

    #     with open(f"{district}/{shop_id}/page_{page}/item_image/{num_iid}.jpg", 'wb') as f:
    #         f.write(response.content)
    #     print("ok")
    #end image downlaod  ====================

    #page item detail
    while True:
        url = f"https://api-gw.onebound.cn/taobao/item_get/?key=t_856 2094008186&&num_iid={num_iid}&is_promotion=1&&lang=zh-CN&secret=20230114&cache=no"
        r = requests.get(url, headers=headers)
        json_obj = r.json()

        if "item" in json_obj.keys():
            if json_obj['item']['format_check'] == "ok":
                break
        time.sleep(1)

    filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/{num_iid}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/{num_iid}.json", 'w') as f:
        json.dump(json_obj, f, indent=4)

    

    #loop for page count
    while page < page_count:
        page += 1
        while True:
            print("start")
            url = f"https://api-gw.onebound.cn/taobao/item_search_shop/?key=t_856 2094008186&&shop_id=57301367&page={page}&sort=&&lang=zh-CN&secret=20230114"
            print(url)
            r = requests.get(url, headers=headers)
            json_obj = r.json()
            if "items" in json_obj.keys():
                print("true")
                break
            time.sleep(1)
        
        filename = f'{district}/{shop_id}/page_{page}/page.json'
        isExist = os.path.exists(filename)

        if isExist is False:
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(f'{district}/{shop_id}/page_{page}/page.json', 'w') as f:
                json.dump(json_obj, f, indent=4)

        for item in json_obj['items']['item']:
            num_iid = item["num_iid"]
            pic_url = item["pic_url"]
            #image download    ====================
            if 'http' not in pic_url:
                pic_url = f"http:{pic_url}"
            response = requests.get(pic_url)
            # if response.status_code == 200:
            #     print("img")

            #     filename = f"{district}/{shop_id}/page_{page}/item_image/{num_iid}.jpg"
            #     os.makedirs(os.path.dirname(filename), exist_ok=True)

            #     with open(f"{district}/{shop_id}/page_{page}/item_image/{num_iid}.jpg", 'wb') as f:
            #         f.write(response.content)
            #     print("ok")
            #end image downlaod  ====================

            #page item detail

            while True:
                url = f"https://api-gw.onebound.cn/taobao/item_get/?key=t_856 2094008186&&num_iid={num_iid}&is_promotion=1&&lang=zh-CN&secret=20230114&cache=no"
                r = requests.get(url, headers=headers)
                json_obj = r.json()

                if "item" in json_obj.keys():
                    if json_obj['item']['format_check'] == "ok":
                        break
                time.sleep(1)

            filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/{num_iid}.json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/{num_iid}.json", 'w') as f:
                json.dump(json_obj, f, indent=4)

        
        time.sleep(3)




if __name__ == "__main__":
    while True:
        print("start")
        r = requests.get(url, headers=headers)
        json_obj = r.json()
        print(json_obj)
        if "items" in json_obj.keys():
            print("true")
            break
        time.sleep(1)
    #anayse first response to get data including page count...
    # print(json_obj['items']['page_count'])

    page = int(json_obj['items']['page'])
    page_count = int(json_obj['items']['page_count'])
    
    #analyse url to get neccessary info
    url_split = url.split("/")

    #district --> example: taobao, 1688, Dangdang...
    district = url_split[3]+"_json"

    #shop id inside district
    shop_id = url_split[5].split("&&")[1].split("&")[0]

    filename = f'{district}/{shop_id}/page_{page}/page.json'
    isExist = os.path.exists(filename)

    if isExist is False:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(f'{district}/{shop_id}/page_{page}/page.json', 'w') as f:
            json.dump(json_obj, f, indent=4)



    for item in json_obj['items']['item']:
        # downloadJson(item, page)
         # downloadImage(filename,f"{prev}/{filename}")
        downloadThread = Thread(target=downloadJson, args=(item, page, ))
        downloadThread.isDaemon = True
        downloadThread.start()

   
