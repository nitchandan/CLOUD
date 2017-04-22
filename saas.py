#!/usr/bin/python

import os,commands,cgi
print "content-type:text/html"
print ""

x=cgi.FieldStorage()
snm=x.getvalue('softy')
unm=x.getvalue('nm')
upwd=x.getvalue('pwd')
a=commands.getstatusoutput("sudo useradd"+" "+unm)
print a
b=commands.getstatusoutput("sudo echo "+upwd+" | sudo  passwd "+ unm + " --stdin")
print b
c=commands.getstatusoutput('sudo touch /'+snm+'.py')
print c
d=commands.getstatusoutput('sudo chmod 777 /'+snm+'.py')
print d
f=open('/'+snm+'.py','w')
f.write("#!/usr/bin/python")
f.write("\nimport os,commands")
f.write("\ncommands.getstatusoutput(\'ssh -X -l  "+unm+" 192.168.122.41 "+snm+"\')")
f.close()
commands.getstatusoutput("sudo tar -cvf  "+snm+".tar  /"+snm+".py")
commands.getstatusoutput("sudo mv "+snm+".tar  /var/www/html/")
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.41/"+snm+".tar\">\n"


