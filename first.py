#!/usr/bin/python

import cgi

print "content-type:text/html"
print ""
x=cgi.FieldStorage()

y=x.getvalue('nm')
print y

y=x.getvalue('sz')
print y

