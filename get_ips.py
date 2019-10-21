import socket

def get_fqdm(url):
    ip = socket.gethostbyname(url)
    print("IP: ", ip)

get_fqdm(str(input("Input URL: ")))
