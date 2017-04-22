#!/usr/bin/python

import cgi,cgitb,commands
cgitb.enable()

import mysql.connector as mariadb
db=mariadb.connect(user='root',password='q',database='cloud')

cursor=db.cursor()
#getting data from the above registration form

detail=cgi.FieldStorage()


u_name=detail.getvalue('nm')
password=detail.getvalue('pwd')
rpassword=detail.getvalue('rpwd')




print "content-type:text/html"

print ""

#inserting into the database


if password == rpassword :
        cursor.execute("INSERT into user VALUES (%s,%s)", (u_name,password))
	print "REgeistered Successfully"
else:
        print"mismatch password"



db.commit()

db.close()

#creating user in the cloud server

#commands.getstatusoutput('sudo useradd '+u_name)
#commands.getstatusoutput('sudo echo '+password+'| sudo passwd '+user+'--stdin'))


#print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.41/home.html\">\n"



