import requests
import json
import mysql.connector


def data_store():
        
    cat_list = [
        # "https://www.udemy.com/courses/development/", 288
        # "https://www.udemy.com/courses/business/",  268
        # "https://www.udemy.com/courses/finance-and-accounting/", 328
        # "https://www.udemy.com/courses/it-and-software/", 294
        # "https://www.udemy.com/courses/office-productivity/", 292
        # "https://www.udemy.com/courses/personal-development/", 296
        # "https://www.udemy.com/courses/design/",  269
        # "https://www.udemy.com/courses/marketing/", 290
        # "https://www.udemy.com/courses/lifestyle/",  274
        # "https://www.udemy.com/courses/photography-and-video/", 273
        # "https://www.udemy.com/courses/health-and-fitness/", 276
        # "https://www.udemy.com/courses/music/",  278
        # "https://www.udemy.com/courses/teaching-and-academics/"  300
    ]

    cookies = {
        '__udmy_2_v57r': 'd017ae875e1a47688766fbb278ab8fe8',
        '__udmy_1_a12z_c24t': 'VGhlIGFuc3dlciB0byBsaWZlLCB0aGUgdW5pdmVyc2UsIGFuZCBldmVyeXRoaW5nIGlzIDQy',
        'csrftoken': 'ZbRs77jTnE8Oc2S0t8vxEU8dts4vAA90w28ObCp4GvycHz45WJmLKj1HZPLwu6QH',
        'ud_cache_brand': 'INen_US',
        'ud_cache_marketplace_country': 'IN',
        'ud_cache_price_country': 'IN',
        'ud_cache_release': 'fe771d53f56b40195120',
        'ud_cache_user': '""',
        'ud_cache_version': '1',
        'ud_cache_language': 'en',
        'ud_cache_device': 'None',
        'ud_cache_logged_in': '0',
        '__cf_bm': 'ISp1EE7Z_DMe6LDYVngcALQWtjdAbv5TYdgSXaluHSI-1690614273-0-AW4Fl+DUveg4jvcP5bb9vJopSSTP9BJEUTFBHDThHrgB5772juZjbCv9UN568/jzKCE9laUD4OLpWRKNgVwPC2o=',
        '__cfruid': '6c5bb59dd18c7a3da1602d8d4fd80a3cf8bd6eb5-1690614273',
        '__udmy_4_a12z': 'e39b2a68941bd33e1a78a09323e98f1bb8f2d4f4b2bcd236660a821b8b97c1e5',
        'cf_clearance': 'uHx3WOvGRfnNpafqehGtWhYO3PefzcuijOg3oPIWAV0-1690614280-0-0.2.1690614280',
        'ud_cache_campaign_code': 'INNVDPP',
        'ud_firstvisit': '2023-07-29T07:04:40.862072+00:00:1qPe0G:8K6wpn4TNxbi2Pb7i8afzvKUlB8',
        '_gid': 'GA1.2.1811546126.1690614282',
        '_gat': '1',
        'ab.storage.deviceId.5cefca91-d218-4b04-8bdd-c8876ec1908d': '%7B%22g%22%3A%22f2777b5e-634f-bbe8-0a66-cf36039ab8d5%22%2C%22c%22%3A1690614283708%2C%22l%22%3A1690614283708%7D',
        '__ssid': '342a5b2be722c6b342f50124d4d1c9e',
        '_gcl_au': '1.1.1377323255.1690614285',
        'blisspoint_fpc': '487f4a30-2005-4d56-b33e-fecc107426de',
        '_rdt_uuid': '1690614285266.13191be7-ba48-4c18-a789-d4ab659eb1f8',
        '_yjsu_yjad': '1690614285.c5cfb089-b993-4ec0-b95a-31b5c3f33a20',
        'ki_t': '1690614286296%3B1690614286296%3B1690614286296%3B1%3B1',
        'ki_r': '',
        'ki_s': '227428%3A0.0.0.0.0',
        '_ga_7YMFEFLR6Q': 'GS1.1.1690614285.1.1.1690614297.0.0.0',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Jul+29+2023+12%3A34%3A57+GMT%2B0530+(India+Standard+Time)&version=202305.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6123365d-ed52-46ac-8088-849a0b8e9fb7&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0005%3A1%2CC0004%3A1%2CC0001%3A1%2CC0002%3A1&AwaitingReconsent=false',
        '_ga': 'GA1.2.1543572972.1690614282',
        'ab.storage.sessionId.5cefca91-d218-4b04-8bdd-c8876ec1908d': '%7B%22g%22%3A%22da5d9d51-e4db-427d-386f-a20d65433f73%22%2C%22e%22%3A1690616102407%2C%22c%22%3A1690614283705%2C%22l%22%3A1690614302407%7D',
        'evi': '"3@O55P_F5JsH4KDQ6mGFbEaYW8RPN--H5C1L4xmm28yL-EsvLavQHB7TT3"',
        'exaff': '%7B%22start_date%22%3A%222023-07-29T07%3A04%3A32.739654Z%22%2C%22code%22%3A%22UGrHaPSUfM0-0B3FPRI12XPrkk0NWMDfdA%22%2C%22merchant_id%22%3A39197%2C%22aff_type%22%3A%22LS%22%2C%22aff_id%22%3A68626%7D:1qPe0g:RvwvViuZ3iu-Vn2V6zEjVt4AV5c',
        'ud_rule_vars': 'eJx9jcsOgjAQRX_FdKuQaXlM7beQNANMoZGksRRdEP5dfC7d3pxzzyoSxYET9_bmZ59CND1IJNZYsaQSa62xrl3bKtTUasfadCFcPAtzEGsjnI9zeru2p8TNvjdCgSoywEydD4AGSlOoHMtSyfMRwAA04rRTE-1qCks32hTJOd_ZOSyxY3uj6KmdPm9DDPc02icx-VfjZ0e-Ljz_SVcG6lwVKGX1TW9iewDakUvg:1qPe0g:cG476N5PW95GrzHmVA4yr2ZR9sI',
        'eventing_session_id': 'Leui1o26Q9CalGfqH9qK5Q-1690616106433',
        '_dd_s': 'rum=0&expire=1690615206727',
    }

    headers = {
        'authority': 'www.udemy.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://www.udemy.com/courses/teaching-and-academics/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-udemy-cache-brand': 'INen_US',
        'x-udemy-cache-campaign-code': 'INNVDPP',
        'x-udemy-cache-device': 'None',
        'x-udemy-cache-language': 'en',
        # 'x-udemy-cache-logged-in': '0',
        # 'x-udemy-cache-marketplace-country': 'IN',
        # 'x-udemy-cache-price-country': 'IN',
        'x-udemy-cache-release': 'fe771d53f56b40195120',
        'x-udemy-cache-user': '',
        'x-udemy-cache-version': '1',
    }

    proxy_handlers={
            "http": "http://b3fa55dc94924b5c9fb14e6aa983522e:@webdataguru.crawlera.com:8011/",
            "https": "http://b3fa55dc94924b5c9fb14e6aa983522e:@webdataguru.crawlera.com:8011/",
        }

    for i in range(1,169):
        params = {
            'p': str(i),
            'page_size': '60',
            'subcategory': '',
            'instructional_level': '',
            'lang': '',
            'price': '',
            'duration': '',
            'closed_captions': '',
            'subs_filter_type': '',
            'category_id': '300',
            'source_page': 'category_page',
            'locale': 'en_US',
            'currency': 'inr',
            'navigation_locale': 'en_US',
            'skip_price': 'true',
            'sos': 'pc',
            'fl': 'cat',
        }
        
        while True:
            response = requests.get(
                'https://www.udemy.com/api-2.0/discovery-units/all_courses/',
                params=params,
                cookies=cookies,
                headers=headers,
                proxies=proxy_handlers,
                verify='zyte-proxy-ca.crt'
            )
            print(response)
            if response.status_code==200 or response.status_code==404 or response.status_code==400:
                break
            else:
                import time
                time.sleep(10)
        
        with open(f'udemy_source_data/teaching-and-academics_{i}.json','w+',encoding='utf-8') as file:
            file.write(response.text)
            print('teaching-and-academics')
            file.close()

        # with open(f'udemy_source_data/music_{i}.json','w+',encoding='utf-8') as file:
        #     file.write(response.text)
        #     print('music')
        #     file.close()

        # with open(f'udemy_source_data/health-and-fitness_{i}.json','w+',encoding='utf-8') as file:
        #     file.write(response.text)
        #     print('health-and-fitness')
        #     file.close()
        print('Total Stored: ',i)
        # break


def fetch_and_store():
    web_id = 3
    web_souce='udemy'
    count=0
    inset_data_list=[]
    try:
        for i in range(1,169):
            with open(f'udemy_source_data/teaching-and-academics_{i}.json','r+',encoding='utf-8') as file:
                raw_data=file.read()
                file.close()
            json_data=json.loads(raw_data)

            category = json_data['unit']['title'].replace('courses','').strip()
            sub_cat=''
            price=''
            start_date='Any-Time'
            university_name='Udemy'
            print('Page No.',i)
            for product_data in json_data['unit']['items']:
                course_name=product_data['title'].strip()
                desc=product_data['headline']
                img = product_data['image_750x422']
                course_url='https://www.udemy.com'+product_data['url']
                try:rating=round(float(product_data['rating']),1)
                except:rating='0'
                try:review=product_data['num_reviews']
                except:review='0'
                course_type=str(product_data['instructional_level'])+' - '+str(product_data['content_info_short'])
                

                price_id=product_data['id']

                
                d_list=(web_id,web_souce,category,sub_cat,course_name,price,start_date,desc,university_name,img,course_url,review,rating,course_type,price_id)
                
                inset_data_list.append(d_list)

                # print(d_list)

                
                count+=1
                print('Total:',count)
    except Exception as e:print(e)
    # print(len(inset_data_list))
    # conn=mysql.connector.connect(**DB_Local)
    # cursor=conn.cursor(buffered=True)
    # commit_c=0
    # for k in inset_data_list:
    #     cursor.execute(f'INSERT INTO master_courses_table values (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',k)
    #     conn.commit()
    #     commit_c+=1
    #     print('Commit:',commit_c)

    # conn.close()


if __name__=='__main__':
    DB_Local = {
        "host":'127.0.0.1',
        "username":'root',
        "password":'super@admin$meet%2232',
        "database":'ecoursefinder',
    }
    fetch_and_store()