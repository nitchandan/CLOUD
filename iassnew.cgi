#!/usr/bin/python
import commands
import cgi
import cgitb
import random
import time
cgitb.enable()
print "content-type:text/html"
print ""

ra=cgi.FieldStorage()
a=ra.getvalue('z')
b=ra.getvalue('x')
c=ra.getvalue('y')
d=ra.getvalue('w')
e=ra.getvalue('v')
f=ra.getvalue('o')
g=ra.getvalue('k')


i=1
while i <= int(g):
	df=random.randint(5900,5930)
	dp=random.randint(5555,5585)
	commands.getstatusoutput("sudo qemu-img create -f qcow2 /var/lib/libvirt/images/{}{}.qcow2 {}G".format(a,i,d))
	im=commands.getstatusoutput("sudo virt-install  --name {0}{4} --ram {1} --vcpu {2} --location http://192.168.122.1/rhel7 --disk /var/lib/libvirt/images/{0}{4}.qcow2 --os-type linux --os-variant  rhel7 --graphics vnc,listen=0.0.0.0,password='redhat',port={3} --hvm --noautoconsole".format(a,c,e,df,i))
	print im
	i=i+1
	commands.getstatusoutput("sudo python /root/Desktop/websockify-master/websockify.py -D 192.168.122.1:{} 192.168.122.1:{}".format(dp,df))
	f=open("/var/www/html/{}".format(a),"a")
	commands.getstatusoutput("sudo chmod 777 /var/www/html/{}.html".format(a))
	f.write("<iframe src='http://192.168.122.1/vnc/index.html?host=192.168.122.1&port={}'".format(dp))
	f.close()
#print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/{}.html\">\n".format(a)
