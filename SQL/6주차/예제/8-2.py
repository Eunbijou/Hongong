Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pymysql
>>> # 전역변수 선언부
con, cur = None, None
>>> data1, data2, data3, data4 = "", "", "", ""
>>> row=None
>>> # 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
>>> cur = conn.cursor()
>>> cur.execute("SELECT * FROM userTable")
5
>>> print("사용자ID    사용자이름    이메일        출생연도")
사용자ID    사용자이름    이메일        출생연도
>>> print("----------------------------------------------------")
----------------------------------------------------
>>> while (True) :
	row = cur.fetchone()
	if row== None :
		break
	data1 = row[0]
	data2 = row[1]
	data3 = row[2]
	data4 = row[3]
	print("%5s   %15s   %20s   %d" % (data1, data2, data3, data4))

	
 hong               홍지윤         hong@naver.com   1996
  kim               김태연           kim@daum.net   2011
 star               별사랑         star@paran.com   1990
 yang               양지은         yang@gmail.com   1993
   su                수지        suji@hanbit.com   1994
>>> conn.close()
>>> 