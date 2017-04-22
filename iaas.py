#!/usr/bin/python

import os,commands,cgi,random,time

print "content-type:text/html"
print ""

x=cgi.FieldStorage()
os=x.getvalue('onm')
hd=x.getvalue('hds')
ram=x.getvalue('rms')
vscp=x.getvalue('vcpu')

print os
print hd
print ram
print vscp
a=commands.getstatusoutput("sudo qemu-img  create -f qcow2  /var/lib/libvirt/images/"+os+".qcow2 "+hd+"G")
print a

po = str(random.randint(5914, 5999))
b=commands.getstatusoutput("sudo virt-install --name "+os+" --memory "+ram+" --vcpus "+vscp+" --os-type linux  --os-variant rhel7  --location ftp://192.168.122.1/pub/rhel7 --disk  /var/lib/libvirt/images/"+os+".qcow2 --noautoconsole --graphics vnc,listen=0.0.0.0,port="+po)
print b
powb = str(random.randint(6000, 8000))

c=commands.getstatusoutput("sudo python /var/www/cgi-bin/websockify-master/websockify.py -D 192.168.122.1:"+powb+"   192.168.122.1:"+po)
print c


print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.1/vnc/index.html?host=192.168.122.1&port="+powb+"\">\n"


