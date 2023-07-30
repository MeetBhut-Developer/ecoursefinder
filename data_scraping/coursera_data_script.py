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

WEB_SOURCE='coursera'
WEB_ID=1

cookies = {
    '__204u': '7190206517-1683439403521',
    'CSRF3-Token': '1690264185.kwTzn15eOteFaaMa',
    '__204r': '',
    '__400v': '6b96c22e-f327-4c8b-922c-3410ea2d5970',
    '__400vt': '1689736462759',
    '__EventPulseVisitId': '93259bd8-56bf-4d47-b13f-900b1264873b~1689735608713',
    '__EventPulseLastActivityTime': '1689736459462',
    '__EventPulseInitialReferrer': 'https%3A%2F%2Fwww.coursera.org',
    'alert_closed_csds_boost': 'true',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'}

count=0
print('---------')
for i in range(1,85):
    params = {
        'query': 'data science',
        'page': str(i),
    }
    while True:
        response = requests.get('https://www.coursera.org/courses', params=params, headers=headers)
        print(response)
        if response.status_code==200 or response.status_code==404:
            break

    xp = HtmlResponse(url='',body=response.text,encoding='utf-8')
    cat='Data Science'
    sub_cat='Data Science'
    start_date='Any-Time'
    price='Free'
    # print(price)
    for data in xp.xpath('//*[@class="cds-9 css-18msmec cds-10"]/li'):
        course_url = 'https://www.coursera.org'+data.xpath('.//a/@href').get('').strip()
        print(course_url)
        course_name=data.xpath('.//h2/text()').get('').strip()
        desc=data.xpath('.//h2/parent::div/p/text()').get('').strip()
        img=data.xpath('.//div[@data-e2e="ProductCard"]//div/img/@src').get('').strip().split('?')[0].strip()
        university=data.xpath('.//div[@data-e2e="ProductCard"]//div[2]//span/text()').get('').strip()
        rating=data.xpath('.//*[contains(@class,"product-reviews")]/p/text()').get('').strip()
        review=data.xpath('.//*[contains(@class,"product-reviews")]/p[2]/text()').get('').strip().split(' ')[0].replace('(','').strip()
        c_type=data.xpath('.//*[contains(@class,"product-reviews")]/following-sibling::p/text()').get('').strip().replace('Â·','-')
        d_list=[WEB_ID,WEB_SOURCE,cat,sub_cat,course_name,price,start_date,desc,university,img,course_url,review,rating,c_type]
        print(d_list)
        # print(d_list)
        # try:
        #     cursor.execute(f'INSERT INTO master_courses_table values (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',d_list)
        #     conn.commit()
        #     count+=1
        #     print('Total Inserted:',count)
        # except:print('Duplicate Data!!!')

conn.close()
    