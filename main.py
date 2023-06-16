import sys, socket
from datetime import datetime

#Defind Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
else:
    print("Invalid Amount of Arguments!")
    print("Syntax: python3 scanner.py <IP>")

# Add a pretty banner
print("-" * 50)
print("Time Started:" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            s.close()
except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname Could not be resolved!")
    sys.exit()
except  socket.error:
    print("Could not connect to server.")
    sys.exit()

