#!/usr/bin/python

import os,commands,cgi

print "content-type:text/html"
print ""

x=cgi.FieldStorage()
nm=x.getvalue('nm')

snp=x.getvalue('dy')
#print nm
print snp

a=commands.getstatusoutput("sudo lvcreate --size 100M --name  " + snp + " -s /dev/cloud/"+nm)
if a[0] == 0:
               print "Success!"

else:
     print"Errora"
        
b=commands.getstatusoutput("sudo mkdir /media/"+snp)
      

      
   
d=commands.getstatusoutput("sudo mount /dev/cloud/"+snp+" /media/"+snp)
commands.getstatusoutput("sudo echo '/media/"+snp+"  *(rw,no_root_squash)' >> /etc/exports")
commands.getstatusoutput("sudo systemctl restart nfs-server")  
#os.system("sudo echo  '/dev/cloud/"+nm+" /media/"+nm+" ext4  defaults  0 0'  >>/etc/fstab")

if d[0] == 0:
               print "Success!"
               
else:
     print"Error"              


  
  
  
   
   

  

   


   
  
