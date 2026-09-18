import socket
import threading
from datetime import datetime

# Set the target to scan (127.0.0.1 is your own local machine)
# You can change this to your router's IP (e.g., 192.168.1.1) to see actual open network ports
TARGET = '127.0.0.1'
PORT_RANGE = range(1, 1025) # Scans the standard "well-known" ports

print("-" * 50)
print(f"Scanning Target: {TARGET}")
print(f"Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 50)

def scan_port(port):
    try:
        # Create a network socket (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Wait a maximum of 1 second for a response
        
        # connect_ex returns 0 if the connection is successful (the port is open)
        result = s.connect_ex((TARGET, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

# Use threading to scan multiple ports simultaneously for speed
threads = []
for port in PORT_RANGE:
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish before closing the script
for thread in threads:
    thread.join()

print("-" * 50)
print("Network scan complete.")
