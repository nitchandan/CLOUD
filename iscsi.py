#!/usr/bin/python

import os,commands,cgi

print "content-type:text/html"
print ""

x=cgi.FieldStorage()
disk=x.getvalue('dm')
trgt=x.getvalue('tm')

sz=x.getvalue('sz')

a=commands.getstatusoutput("sudo lvcreate --size  " + sz+"M --name  " + disk + "  cloud")
print trgt
print disk
print sz
b="<target "+trgt+"> \n  backing-store  /dev/cloud/"+disk+"   \n  </target>"
commands.getstatusoutput("sudo touch /"+disk+".conf")
commands.getstatusoutput("sudo chmod 777 /"+disk+".conf")
f=open('/'+disk+'.conf', 'w')
f.write(b)
f.close()

commands.getstatusoutput("sudo mv /" + disk+".conf /etc/tgt/conf.d/")








f=commands.getstatusoutput("sudo systemctl restart  tgtd")
if f[0] == 0:
               print "Success!"
               commands.getstatusoutput("sudo iptables -F")
               commands.getstatusoutput("sudo touch /"+disk+".py")
	       commands.getstatusoutput("sudo chmod 777 /"+disk+".py")
               f=open('/'+disk+'.py', 'w')
               f.write("#!/usr/bin/python")
               f.write("\nimport os,commands")
       
               f.write("\ncommands.getstatusoutput(\' iscsiadm --mode discoverydb  --type sendtargets  --portal 192.168.122.41  --discover\')") 
               f.write("\ncommands.getstatusoutput(\' iscsiadm --mode node --targetname "+trgt+"  --portal 192.168.122.41:3260   --login\' )")
               f.close()
          

	       awq=commands.getstatusoutput("sudo tar  -cvf " + disk+".tar  /"+disk+".py")	
              
	       bzs=commands.getstatusoutput("sudo mv " + disk+".tar /var/www/html/")	
	       print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.41/"+disk+".tar\">\n"
	       
       

else :
       print "EXPORT FILE ERROR" 


  
  
  
   
   

  

   


   
  
