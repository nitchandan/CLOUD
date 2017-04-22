#!/usr/bin/python

import os,commands,cgi

print "content-type:text/html"
print ""

x=cgi.FieldStorage()
nm=x.getvalue('nm')

sz=x.getvalue('sz')


commands.getstatusoutput("sudo lvextend --size +"+sz+"M /dev/cloud/"+nm)
commands.getstatusoutput("sudo resize2fs /dev/cloud/"+nm)

