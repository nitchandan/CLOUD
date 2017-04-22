#!/usr/bin/python
import cgi,commands,cgitb
cgitb.enable()


print "content-type:text/html"
print ""




form=cgi.FieldStorage()

x=form.getvalue('a')
y=form.getvalue('b')
z=form.getvalue('c')

commands.getstatusoutput("sudo touch /paas/{}.sh".format(x))
commands.getstatusoutput("sudo chmod 777 /paas/{}.sh".format(x))
f=open("/paas/{}.sh".format(x),"w")
f.write("#!/bin/bash\n\nuseradd -s /usr/bin/python {}\necho {}| passwd {} --stdin".format(x,y,x))
f.close()
k=commands.getstatusoutput("sudo docker run -itd -v /paas:/media/ rahul1 ")
j=k[1]
commands.getstatusoutput("sudo docker exec {} /media/{}.sh".format(j,x))
commands.getstatusoutput("sudo docker exec {} service sshd restart".format(j))
v=commands.getstatusoutput("sudo docker exec {} hostname -i".format(j))
commands.getstatusoutput("sudo docker exec {0} sed -Ei 's/172.17.0.2/{1}/g' /etc/sysconfig/shellinaboxd".format(j,v[1]))
commands.getstatusoutput("sudo docker exec -t {} service shellinaboxd restart".format(j))
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://{}:4200\">\n".format(v[1])


