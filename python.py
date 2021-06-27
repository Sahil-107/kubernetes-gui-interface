#!/usr/bin/python3
import cgi
import subprocess

print("Access-Control-Allow-Origin:*")
print("content-type: text/html")
print()

s=cgi.FieldStorage()
cmd=s.getvalue("x").split()
print(cmd)

if "deployment" and "create" in cmd :
    run_cmd= f"kubectl create deployment {cmd[2]} --image={cmd[3]}"

if "create" and "pod" in cmd:
    print("Running pod please wait ...\n")
    run_cmd = f"kubectl run {cmd[2]} --image={cmd[3]}"
    print(run_cmd)

elif "expose" and "service" in cmd :
    run_cmd = f"kubectl expose {cmd[1]} {cmd[2]}"


elif "destroy" and "all" in cmd:
    run_cmd= f"kubectl delete all --all"


elif "delete" in cmd:
    run_cmd= f"kubectl delete {cmd[1]} {cmd[2]}"


elif "scale" in cmd:
    run_cmd= f"kubectl scale {cmd[1]}/{cmd[2]} --replicas={cmd[3]}"


print(run_cmd)
check_out = subprocess.getoutput(f"{run_cmd}")
#check_out = subprocess.run(f"{run_cmd}",shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print("<br>")
print("<pre>")
#if check_out.returncode != 0 :
#    print(f"Some error happend\n\n{check_out.stderr}")
    
#else :
#    print(f"{check_out.stdout}")
print(check_out)
print("</pre>")
    
    






