# Author: PiereLucas(Julian Huch)
# Creation: 22.10.2019
# Last update: 22.10.2019w

"""
Tor Ip Switcher - We have to use a different exit Node for ervery thread to make das DoS attack look like a
DDoS attack.
"""

# This module is under dev.
# Don't use

# Dist Modules
import os
import sys
import time
from stem import Signal
from stem.control import Controller
# Site Modules
from modules.colorama import Fore

# Colors
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Fore.RESET


def check_for_file():
    try:
        if os.path.isfile("../tor_pass.txt"):
            with open("../tor_pass.txt", 'rt') as f:
                tor_pass = f.read()
                if tor_pass == "":
                    print("tor_pass file is empty")
                    sys.exit(0)
        else:
            tor_pass = str(input("Tor Control Password » "))
            with open("../tor_pass.txt", 'wt') as f:
                f.write(tor_pass)
    except PermissionError as ex:
        print("no read/write permission :", ex)
        sys.exit(0)
    else:
        return tor_pass

def switch_ip(tor_pass):
    while True:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(tor_pass)
            controller.signal(Signal.NEWNYM)
            print("New TOR Circuit loaded ...")
            time.sleep(10)