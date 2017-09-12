
#coding=utf-8

import pymysql.cursors


#获取链接
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='wikiurl',
    charset='utf8mb4'
)

#获取会话指针

try:
    with connection.cursor() as cursor:
        sql = "select `urlname`,`urlhref` from `urls` WHERE id is NOT NULL "
        count = cursor.execute(sql)
        print  count

        rs = cursor.fetchmany(size=9)
        print rs
finally:
    connection.close()
