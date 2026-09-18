import socket

target = '127.0.0.1' # Checking my own machine

print("Scanning for open ports...")

# Just checking the first 100 ports for simplicity
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Wait half a second before giving up
    
    # connect_ex tries to connect. If it returns 0, it was successful!
    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is OPEN")
        
    s.close()

print("Scan complete.")
