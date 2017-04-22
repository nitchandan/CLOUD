#!/usr/bin/python

import os,commands,cgi,cgitb
cgitb.enable()

print "content-type:text/html"
print ""

x=cgi.FieldStorage()


day=x.getvalue('dy')


      
commands.getstatusoutput("sudo touch /"+day+".py")
commands.getstatusoutput("sudo chmod 777 /"+day+".py")
f=open('/'+day+'.py', 'w')
f.write("#!/usr/bin/python")
f.write("\nimport os,commands")
f.write("\ncommands.getstatusoutput(\'mkdir /media/"+day+"\')")
f.write("\ncommands.getstatusoutput(\'mount 192.168.122.41:/media/"+day+" /media/"+day+"\')")
f.close()
awq=commands.getstatusoutput("sudo tar  -cvf " + day+".tar  /"+day+".py")	
bzs=commands.getstatusoutput("sudo mv " + day+".tar /var/www/html/")
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.41/"+day+".tar\">\n"

	       
 


  
  
  
   
   

  

   


   
  
