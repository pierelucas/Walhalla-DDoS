#
# Modules
#
import os, sys, time, subprocess
import socket, threading
from colorama import Fore, Style
from progressbar import Bar

class Walhalla():

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
        self.threads = None
        self.num_req = None

    def input(self):
        pass

    def out(self):
        print(self.banner_txt)

    def run(self):
        self.input()
        self.out()

# TO BE CONTINUED ...
walhalla = Walhalla()
walhalla.run()
