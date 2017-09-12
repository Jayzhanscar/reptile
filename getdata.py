#coding=utf-8

import urllib2

from bs4 import  BeautifulSoup

import re



import pymysql.cursors
'''
访问 维基百科的 词条链接
'''
req = urllib2.Request('https://en.wikipedia.org/wiki/Wiki')
response = urllib2.urlopen(req)
the_page = response.read().decode('utf-8')
print the_page

soup = BeautifulSoup(the_page,'html.parser')

listUrl = soup.find_all('a',href=re.compile("^/wiki/"))


for url in listUrl:
    if not re.search("\.(jpg|JPG)$",url['href']):
        print url.get_text(),'<------------->','https://en.wikipedia.org/wiki/Wiki'+url['href']

        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='wikiurl',
            charset='utf8mb4'
        )


        try:
            with connection.cursor() as cursor :
                sql = "insert into `urls`(`urlname`,`urlhref`)VALUES (%s,%s)"

                cursor.execute(sql,(url.get_text(),'https://en.wikipedia.org/wiki/Wiki'+url['href']))

                connection.commit()



        finally:
            connection.close()
