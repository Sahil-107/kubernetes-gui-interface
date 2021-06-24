#!/usr/bin/python3
import cgi
import subprocess
import time
print("Access-Control-Allow-Origin:*")
print("content-type: text/html")
print()

s=cgi.FieldStorage()
cmd=s.getvalue("x")

if "deployment" and "create" and "centos" in cmd :
    cmd= "kubectl create deployment mydep --image=centos"
    output = subprocess.getoutput("sudo "+cmd)

elif "deployment" and "create" and "ubuntu" in cmd:
    cmd= "kubectl create deployment mydep --image=centos"
    output = subprocess.getoutput("sudo "+cmd)

elif cmd=="run":
    cmd= "docker run -dit "+ s.getvalue("y")
    output = subprocess.getoutput("sudo "+ cmd)

elif cmd=="exec":
    cmd= "docker exec -i "+ s.getvalue("y")+" "+s.getvalue("z")
    output = subprocess.getoutput("sudo "+ cmd)

elif cmd=="download":
    cmd= "docker pull "+ s.getvalue("y")
    output = subprocess.getoutput("sudo "+ cmd)

elif cmd=="rmi":
    cmd= "docker rmi "+s.getvalue("y")+" --force"
    output = subprocess.getoutput("sudo "+ cmd)

print("<br>")
print("<pre>")
print(output)
print("</pre>")



