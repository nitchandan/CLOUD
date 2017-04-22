#!/usr/bin/python

import os,commands,cgi

print "content-type:text/html"
print ""

x=cgi.FieldStorage()
nm=x.getvalue('nm')

sz=x.getvalue('sz')

a=commands.getstatusoutput("sudo lvcreate --size  " + sz+"M --name  " + nm + "  cloud")

b=commands.getstatusoutput("sudo mkdir /media/"+nm)
      
c=commands.getstatusoutput("sudo mkfs.ext4  /dev/cloud/"+nm)
      
   
d=commands.getstatusoutput("sudo mount /dev/cloud/"+nm+" /media/"+nm)  
#os.system("sudo echo  '/dev/cloud/"+nm+" /media/"+nm+" ext4  defaults  0 0'  >>/etc/fstab")

e=commands.getstatusoutput("sudo echo '/media/"+nm+"  *(rw,no_root_squash)' >> /etc/exports")
if e[0] == 0:
       f=commands.getstatusoutput("sudo systemctl restart nfs-server")
       if f[0] == 0:
               print "Success!"
               
               commands.getstatusoutput("sudo touch /"+nm+".py")
	       commands.getstatusoutput("sudo chmod 777 /"+nm+".py")
               f=open('/'+nm+'.py', 'w')
               f.write("#!/usr/bin/python")
               f.write("\nimport os,commands")
               f.write("\ncommands.getstatusoutput(\'yum install nfs-utils\')")
               f.write("\ncommands.getstatusoutput(\'showmount -e 192.168.122.41\')")
               f.write("\ncommands.getstatusoutput(\'mkdir /media/"+nm+"\')")
               f.write("\ncommands.getstatusoutput(\'mount 192.168.122.41:/media/"+nm+" /media/"+nm+"\')")
               f.close()
	       awq=commands.getstatusoutput("sudo tar  -cvf " + nm+".tar  /"+nm+".py")	
              
	       bzs=commands.getstatusoutput("sudo mv " + nm+".tar /var/www/html/")	
	       print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.122.41/"+nm+".tar\">\n"
	       
       else:
               print"NFS-ERROR"

else :
       print "EXPORT FILE ERROR" 


  
  
  
   
   

  

   


   
  
