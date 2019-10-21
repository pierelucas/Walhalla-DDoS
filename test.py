import socket

def get_fqdm(url):
    ip = socket.gethostbyname(url)
    print(ip)

get_fqdm("5.9.108.139")
