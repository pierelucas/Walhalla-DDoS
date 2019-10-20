#
# Modules
#
import os, sys, time, subprocess
import socket
from colorama import Fore, Style
from argparse import ArgumentParser

class Dos():

    def tcp_flood(self, ip):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, 80))
            pass

    def udp_flood(self, ip):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(data, (ip, 80))

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
        args = parser.parse_args()
        _true = self.check_args(args)
        if _true:
            return args.target_addr, args.dos_mode

    def check_args(self, args):
        if args.target_addr and args.dos_mode:
            return True
        elif args.target_addr:
            print("Please define dos mode [tcp/udp]")
            sys.exit(0)
        elif arg.dos_mode:
            print("Please define target adress")
            sys.exit(0)
        else:
            print("Use -h or --help for futher information")
            sys.exit(0)

    def get_fqdm(self, target_addr):
        target_ip = socket.gethostbyname(target_addr)
        return target_ip

    def out(self):
        print(Fore.CYAN + self.banner_txt)
        print(Style.RESET_ALL)

    def threads(self):
        pass

    def run(self):
        target_addr, dos_mode = self.arguments()
        target_ip = self.get_fqdm(target_addr)

if __name__ == "__main__":
    cc = Controller()
    cc.run()
