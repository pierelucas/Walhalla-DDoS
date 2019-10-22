# Author: PiereLucas(Julian Huch)
# This script is just for a earlier discover of IP adresses
# It has explicitly nothing to do with walhalla

import socket

def get_fqdm(url):
    ip = socket.gethostbyname(url)
    print("IP: ", ip)

get_fqdm(str(input("Input URL: ")))
