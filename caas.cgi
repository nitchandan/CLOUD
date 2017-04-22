#!/usr/bin/python


print "content-type:text/html"
print  ""


import cgi,commands,cgitb,time,signal
cgitb.enable()


form=cgi.FieldStorage()
x=form.getvalue('a')
y=form.getvalue('b')
z=form.getvalue('c')
 

commands.getstatusoutput("sudo touch /caas/{}.sh".format(x))

commands.getstatusoutput("sudo chmod 777 /caas/{}.sh".format(x))
f=open("/caas/{}.sh".format(x),"w")
f.write("#!/bin/bash\nuseradd {0}\necho {1}|passwd {0} --stdin".format(x,y))
f.close()
port=5790
i=1
while i<=int(z) : 
	p=commands.getstatusoutput ("sudo docker run -itd --privileged -v /caas:/media/caas -p {}:4200 rahul1 /bin/bash".format(port))
	commands.getstatusoutput ("sudo docker exec {} /media/caas/{}.sh".format(p[1],x))
	i=i+1
	commands.getstatusoutput("sudo docker exec {} service sshd restart".format(p[1]))
	v=commands.getstatusoutput("sudo docker exec {} hostname -i".format(p[1]))
	commands.getstatusoutput("sudo docker exec {} sed -Ei 's/172.17.0.2/{}/g' /etc/sysconfig/shellinaboxd".format(p[1],v[1]))
	we1=commands.getstatusoutput("sudo docker exec -t {}  service shellinaboxd restart ".format(p[1]))
	print we1
	f1=open("/var/www/html/{}.html".format(x),"a")
	f1.write("<a href='http://192.168.122.1:{}' target='_blank'>docker</a>\n".format(port))
	f1.close()
	port=port+1

commands.getstatusoutput("sudo chmod 777 /var/www/html/{}.html".format(x))
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/{}.html\">\n".format(x)	




