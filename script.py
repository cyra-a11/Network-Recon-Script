import subprocess # a module to run terminal cmd in py
import socket # handles dns tasks

target= input("Enter the Domain/IP:\n") #taking input
def is_ip(target): #checking if target is an ip
    try:
        socket.inet_aton(target) #checking function
        return True
    except socket.error:
        return False
    
domain ="N/A"
ip="N/A"
if is_ip(target):#calling is_ip function to check ip
    try:
        domain =socket.gethostbyaddr(target)[0] # if ip --> domain
        ip=target
    except socket.herror:
        domain= target #if domain not found
else:
    try:
        ip = socket.gethostbyname(target) # if domain --> ip
        domain=target
    except socket.gaierror:
        ip =target

def ping(target):
    result=subprocess.run(
        ["ping","-n","1",target] #pinging target
    )
    return result.returncode == 0  #ping success
if ping(target):
    update="host is alive"
else:
    update="host is dead"

ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
open_port=[] #making a list
def try_port(target,port):
    s =socket.socket() # creating a tcp socket
    s.settimeout(0.1) # time for scanning each port

    try:
        s.connect((target,port)) #connecting to port
        return True
    except:
        return False
    
for port in ports:
    if try_port(target,port):
        open_port.append(port)
print(f"+ Open Ports: {open_port}")

nscan_ports=len(ports)
nopen_ports=len(open_port)

print(f"\n----Scanning Result----")
print(f"+ Target: {target}")
print(f"+ Resolved Domain: {domain}")
print(f"+ Resolved IP: {ip}")
print(f"+ PING: {update}")
print(f"\n+ Scanned Ports: {nscan_ports}")
print(f"+ Opened Ports: {nopen_ports}")


        

