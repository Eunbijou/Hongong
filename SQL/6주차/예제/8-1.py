Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pymysql
>>> # 전역변수 선언부
conn, cur = None, None
>>> data1, data2, data3, data4 = "", "", "", ""
>>> sql=""
>>> # 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
>>> cur = conn.cursor()
>>> while (True) :
    data1 = input("사용자 ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)

    
사용자 ID ==> su
사용자 이름 ==> 수지
사용자 이메일 ==> suji@hanbit.com
사용자 출생연도 ==> 1994
1
사용자 ID ==> 
>>> conn.commit()
>>> conn.close()
>>> 