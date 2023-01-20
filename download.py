
from __future__ import print_function
import requests
import json
import os
import time

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

if __name__ == "__main__":
    r = requests.get(url, headers=headers)
    json_obj = r.json()
    print(json_obj)

    #anayse first response to get data including page count...
    # print(json_obj['items']['page_count'])

    page = int(json_obj['items']['page'])
    page_count = int(json_obj['items']['page_count'])
    
    #analyse url to get neccessary info
    url_split = url.split("/")

    #district --> example: taobao, 1688, Dangdang...
    district = url_split[3]

    #shop id inside district
    shop_id = url_split[5].split("&&")[1].split("&")[0]

    filename = f'{district}/{shop_id}/page_{page}/{page}.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(f'{district}/{shop_id}/page_{page}/{page}.json', 'w') as f:
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

        url = f"https://api-gw.onebound.cn/taobao/item_get/?key=t_856 2094008186&&num_iid={num_iid}&is_promotion=1&&lang=zh-CN&secret=20230114&cache=no"
        r = requests.get(url, headers=headers)
        json_obj = r.json()

        filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/{num_iid}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/{num_iid}.json", 'w') as f:
            json.dump(json_obj, f, indent=4)

        #images
        #--pic_url image
        pic_url = json_obj['item']['pic_url']
        if 'http' not in pic_url:
            pic_url = f"http:{pic_url}"
        response = requests.get(pic_url)
        if response.status_code == 200:
            filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/pic_url/{num_iid}.jpg"
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/pic_url/{num_iid}.jpg", 'wb') as f:
                f.write(response.content)

        #--items_image
        item_len = len(json_obj['item']['item_imgs']) 
        if item_len > 0:
            for i in range(item_len):
                item_img = json_obj['item']['item_imgs'][i]['url']

                if 'http' not in item_img:
                    item_img = f"http:{item_img}"
                response = requests.get(item_img)

                if response.status_code == 200:
                    filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/item_imgs/{i}.jpg"
                    os.makedirs(os.path.dirname(filename), exist_ok=True)

                    with open(f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/item_imgs/{i}.jpg", 'wb') as f:
                        f.write(response.content)
        #--desc_image
        desc_len = len(json_obj['item']['desc_img']) 
        if desc_len > 0:
            for i in range(desc_len):
                desc_img = json_obj['item']['desc_img'][i]

                if 'http' not in desc_img:
                    desc_img = f"http:{desc_img}"
                response = requests.get(desc_img)

                if response.status_code == 200:
                    filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/desc_imgs/{i}.jpg"
                    os.makedirs(os.path.dirname(filename), exist_ok=True)

                    with open(f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/desc_imgs/{i}.jpg", 'wb') as f:
                        f.write(response.content)
        #--pros_image
        prop_len = len(json_obj['item']['prop_imgs']['prop_img']) 
        if prop_len > 0:
            for i in range(prop_len):
                prop_img = json_obj['item']['prop_imgs']['prop_img'][i]['url']

                if 'http' not in prop_img:
                    prop_img = f"http:{prop_img}"
                response = requests.get(prop_img)

                if response.status_code == 200:
                    filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/prop_imgs/{i}.jpg"
                    os.makedirs(os.path.dirname(filename), exist_ok=True)

                    with open(f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/images/prop_imgs/{i}.jpg", 'wb') as f:
                        f.write(response.content)
        #--video
        # video_len = len(json_obj['item']['video'])
        # if video_len > 0:
        #     video_url = json_obj['item']['video']['url']
            
        #     # import urllib2
        #     import urllib.request as urllib2


        #     # file_name = 'trial_video.mp4' 
        #     filename = f"{district}/{shop_id}/page_{page}/item_detail/{num_iid}/video/1.mp4"
        #     os.makedirs(os.path.dirname(filename), exist_ok=True)

        #     rsp = urllib2.urlopen(video_url)

        #     with open(filename,'wb') as f:
        #         f.write(rsp.read())

        #end images


        #end item detail 


    #loop for page count
    while page < page_count:
        page += 1
        url = f"https://api-gw.onebound.cn/taobao/item_search_shop/?key=t_856 2094008186&&shop_id=57301367&page={page}&sort=&&lang=zh-CN&secret=20230114"
        print(url)
        r = requests.get(url, headers=headers)
        json_obj = r.json()
        
        filename = f'{district}/{shop_id}/page_{page}/{page}.json'
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(f'{district}/{shop_id}/page_{page}/{page}.json', 'w') as f:
            json.dump(json_obj, f, indent=4)
        
        time.sleep(3)



