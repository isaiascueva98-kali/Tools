import socket

target = "192.168.1.1"
ports = [22, 80, 443, 3306, 5432, 8080, 8443]

for port in ports:
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((target,port)) 

        if result == 0:
            print(f"Port {port} is OPEN.")

        else:
            print(f"Port {port}, is CLOSED.")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

    finally:
        s.close()
