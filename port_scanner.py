import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = input("Enter Target IP Addr: ")

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

print("Port" + "   " + "State")
print("----" + "   " + "-----")
for x in range(1,1024):
    if pscan(x):
        print("", x , "   " + "Open")

# This is standerd Port Scanner from "WarmSurface."
