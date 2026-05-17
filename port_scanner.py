import socket
import sys

def ip_address_function():
    
    choice = input("enter 1. for ip address \n 2. for domain name\n")
    
    if choice == "1":
        ip_address = input("enter the ip address:")
    else:
        try:
            ip_address = socket.gethostbyname(input("enter the website name"))
        except socket.gaierror:
            print("invalid hostname")
            sys.exit()
    return ip_address
        

def port_function():

    choice = input("enter\n 1. for single port\n 2. for multiple port\n")

    if choice == "1":
        port = int(input("enter the port number:"))
        port = [port]
    else:
        port=input("enter the range(example:1-10)")
        
        port_split = port.split("-")
        
        port_starting = int(port_split[0])
        port_ending = int(port_split[1])
        
        port = [i for i in range(port_starting,port_ending + 1)]
    return port
        
def main():
    ip_address = ip_address_function()
    port = port_function()
    print("Target:", ip_address)
    if len(port) == 1:
        print(f"ports to scan are {port}")
    else:
        print(f"ports to scan are {port[0]} , {port[-1]}")
    for p in port:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((ip_address,p))
        if result == 0:
            print(f"port {p} is open")
        s.close()
        
    
    
if __name__=="__main__":
    main()

    
