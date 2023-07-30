import requests

cookies = {
    '_gcl_au': '1.1.1943725976.1690085450',
    'twk_idm_key': 'NFRXIffpi8PFL5IF5mtU4',
    '_gid': 'GA1.2.494268806.1690085475',
    '_ga': 'GA1.1.773259515.1690085452',
    '_ga_7P19PEB3F9': 'GS1.1.1690085452.1.1.1690085718.0.0.0',
    'TawkConnectionTime': '0',
    'twk_uuid_5f984696aca01a1688362e64': '%7B%22uuid%22%3A%221.1hH4g6kQml6ONwyPFxY92wlcJWqUthGoN14aVYYF3CwMiQzN6CgXfg99imU0NgV8zkIJZn7QEk89dlmVyCCxPR39kjbmtDT2Ebvbqi6MBFKJ5AokPFo%22%2C%22version%22%3A3%2C%22domain%22%3A%22ineuron.ai%22%2C%22ts%22%3A1690085718426%7D',
}

headers = {
    'authority': 'ineuron.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"2265bf-zzohieFZldTPxS/Ezsxx07fPe8I"',
    'referer': 'https://ineuron.ai/category/DATA-SCIENCE',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

# response = requests.get(
#     'https://ineuron.ai/_next/data/PTbnMoa9fxydgm2EyTmcl/category/DATA-SCIENCE.json',
#     cookies=cookies,
#     headers=headers,
# )

# print(response)
# with open('ineuron_data.json','w+',encoding='utf-8') as file:
#     file.write(response.text)
#     file.close()

DB_Local = {
    "host":'127.0.0.1',
    "username":'root',
    "password":'super@admin$meet%2232',
    "database":'ecoursefinder',
}
import mysql.connector
conn=mysql.connector.connect(**DB_Local)
cursor=conn.cursor(buffered=True)

import json
file = open('ineuron_data.json','r')
json_data = json.loads(file.read())

data = json_data['pageProps']['initialState']['init']['courses']
all_cats = json_data['pageProps']['initialState']['init']['categories']

for cat in all_cats.items():
    main_cat_name = cat[1]['title']
    # print(main_cat)
    sub_cat_dic = cat[1]['subCategories']
    for sub_cat in sub_cat_dic.items():
        sub_cat_id=sub_cat[0]
        sub_cat_name=sub_cat[1]['title']
        # print(main_cat_name,'==>',sub_cat_name)
        # break
    # break


# input()
count=0
for raw in data.items():
    course_name=raw[0]
    category_id=raw[1]['categoryId']
    for cat in all_cats.items():
        main_cat_name = cat[1]['title']
        # print(main_cat)
        sub_cat_dic = cat[1]['subCategories']
        for sub_cat in sub_cat_dic.items():
            sub_cat_id=sub_cat[0]
            sub_cat_name=sub_cat[1]['title']
            if sub_cat_id==category_id:
                course_url='https://ineuron.ai/course/'+course_name.strip().replace(' ','-')
                try:price=str(raw[1]['pricing']['IN'])
                except:
                    price=raw[1]['pricing']['isFree']
                    if price==True:price='Free'
                if price=='0' or price=='':price='Free'

                try:start_date=raw[1]['classTimings']['timings']
                except:
                    try:start_date=raw[1]['classTimings']['startDate']
                    except:start_date='Not-Scheduling'
                
                desc=raw[1]['description']
                img='https://cdn.ineuron.ai/assets/uploads/thumbnails/'+raw[1]['img']

                # print(img)
                d_list=['2','ineuron',main_cat_name,sub_cat_name,course_name,price,start_date,desc,'Private Institute',img,course_url,'','','Anyone']
                # print(d_list)
                try:
                    cursor.execute(f'INSERT INTO master_courses_table values (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',d_list)
                    conn.commit()
                    count+=1
                    print('Total Inserted:',count)
                except:print('Duplicate Data!!!')