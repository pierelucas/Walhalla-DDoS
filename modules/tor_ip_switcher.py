# Author: PiereLucas(Julian Huch)
# Creation: 22.10.2019
# Last update: 22.10.2019w

# Dist Modules
from stem import Signal
from stem.control import Controller

def switch_ip(*, tor_pass):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(tor_pass)
        controller.signal(Signal.NEWNYM)
        return True
