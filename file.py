#!/usr/bin/python
import cgi,os

import cgitb;cgitb.enable()


form=cgi.FieldStorage()

fileitem=form['filename']
if fileitem.filename:
                   fn=os.path.basename(fileitem.filename)
                   open('/tmp/'+fn,'wb').write(fileitem.file.read())
                   msg="The file "+fn+"was loaded successfully"
else:
    msg="No file was loaded succesfully"

print "content-type:text/html"
print ""
print msg

          
