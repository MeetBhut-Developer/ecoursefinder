import requests
from scrapy.http import HtmlResponse
import mysql.connector

DB_Local = {
    "host":'127.0.0.1',
    "username":'root',
    "password":'super@admin$meet%2232',
    "database":'ecoursefinder',
}
conn=mysql.connector.connect(**DB_Local)
cursor=conn.cursor(buffered=True)

cookies = {
    'CSRF3-Token': '1690265357.vzJyvrvmnOXazUeF',
    '__204u': '2514973537-1689401357361',
    '__204r': '',
    '__400v': '960f19cb-18f9-4f72-af98-24d968ee70fe',
    '__EventPulseVisitId': '7079bf07-c409-40c8-a94c-dc585b142aec~1689401360767',
    '_ga': 'GA1.1.2091280289.1689401365',
    'IR_gbd': 'coursera.org',
    'usprivacy': '1---',
    '_gcl_au': '1.1.1102889268.1689401366',
    '_rdt_uuid': '1689401367147.a506c314-39a4-4881-bb63-e5b848835dbf',
    'FPID': 'FPID2.2.9d%2F70PKiC5c6eylLh%2BBK2kBG3b6oaRrV0mgx4QT13mQ%3D.1689401365',
    'FPLC': 'dakIuDCAxJc96CBfljvlgt%2F7g1NKXDpg%2FY3bBizGrtLZ%2Bv3ZiON7jnEv6lfPKgkAFRTJrqohyeePoZf7G%2F%2Bq2NR92z9as9Vj%2BxvmnyzCBRHx%2B9KkL5u16mp2%2F2PrTg%3D%3D',
    '_fbp': 'fb.1.1689401369181.226120209',
    'g_state': '{"i_p":1689408573552,"i_l":1}',
    'OneTrustWPCCPAGoogleOptOut': 'false',
    '__EventPulseInitialReferrer': 'https%3A%2F%2Fwww.coursera.org',
    'maId': '{"cid":"da615de313754d054e60bf808342eb3d","sid":"0233864c-c015-4dae-83b5-5c2ac5b81d44","isSidSaved":true,"sessionStart":"2023-07-15T06:13:46.000Z"}',
    '__EventPulseLastActivityTime': '1689401675613',
    '_ga_ZCE2Q9YZ3F': 'GS1.1.1689401364.1.1.1689401675.3.0.0',
    'IR_14726': '1689401676619%7C0%7C1689401676619%7C%7C',
    '_uetsid': '2763409022d611eeac831f8a7673a02a',
    '_uetvid': '2763daf022d611eebc23192623760fef',
    '_tq_id.TV-63455409-1.39ed': '2e40a6dcae7b6617.1689401368.0.1689401678..',
    '_ga_7GZ59JSFWQ': 'GS1.1.1689401367.1.1.1689401677.0.0.0',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Sat+Jul+15+2023+11%3A44%3A38+GMT%2B0530+(India+Standard+Time)&version=6.10.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=IN%3BTG',
    'OptanonAlertBoxClosed': '2023-07-15T06:14:38.042Z',
    '__400vt': '1689401685028',
}

headers = {
    'authority': 'www.coursera.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
count=0
print('---------')
for i in range(85):
    params = {
        'query': 'python',
        'page': str(i),
    }
    while True:
        response = requests.get('https://www.coursera.org/courses', params=params, cookies=cookies, headers=headers)
        print(response)
        if response.status_code==200 or response.status_code==404:
            break

    xp = HtmlResponse(url='',body=response.text,encoding='utf-8')

    cat='Data Science'
    sub_cat='Python'
    start_date='Any-Time'
    price='Free'

    for data in xp.xpath('//*[@class="cds-9 css-18msmec cds-10"]/li'):
        course_url = 'https://www.coursera.org'+data.xpath('.//a/@href').get('').strip()
        course_name=data.xpath('.//h2/text()').get('').strip()
        desc=data.xpath('.//h2/parent::div/p/text()').get('').strip()
        img=data.xpath('.//div[@data-e2e="ProductCard"]//div/img/@src').get('').strip().split('?')[0].strip()
        university=data.xpath('.//div[@data-e2e="ProductCard"]//div[2]//span/text()').get('').strip()
        rating=data.xpath('.//*[contains(@class,"product-reviews")]/p/text()').get('').strip()
        review=data.xpath('.//*[contains(@class,"product-reviews")]/p[2]/text()').get('').strip().split(' ')[0].replace('(','').strip()
        c_type=data.xpath('.//*[contains(@class,"product-reviews")]/following-sibling::p/text()').get('').strip().replace('Â·','-')
        d_list=[cat,sub_cat,course_name,price,start_date,desc,university,img,course_url,review,rating,c_type]
        cursor.execute(f'INSERT INTO course_master_data values (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',d_list)
        conn.commit()
        count+=1
        print('Total Inserted:',count)

conn.close()
    