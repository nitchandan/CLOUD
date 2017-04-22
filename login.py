#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()


detail=cgi.FieldStorage()
user=detail.getvalue('nm')
password=detail.getvalue('pwd')

print "content-type:text/html"

print ""

#x=open('/var/www/html/user_log',mode='w')
#x.write('{}'.format(user))
#x.close()

import mysql.connector as mariadb


db=mariadb.connect(user='root',password='q',database='cloud')

cursor=db.cursor()


cursor.execute("SELECT password FROM user WHERE name=%s",(user,))

row=cursor.fetchall()

cursor.close()
db.close()



for i in row:
	passwd=i[0]
		

if passwd==password :

	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.41/CCSP\">\n"

else:
	print "NOT AUTHORISED"



