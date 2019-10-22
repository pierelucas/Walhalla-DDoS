#### Walhalla DDoS → A Simple Python DDoS Script

##### Usage:

    ./walhalla.py [-h] [-t TARGET_ADDR] [-p PORT] [-m DOS_MODE] [-a AMOUNT]
                   [-bs BUFFER_SIZE]
    
    ./walhalla.py -h --help
        FOR HELP
    
    -t TARGET_ADDR, --target TARGET_ADDR
        IN FORMAT [www.domain.com]
    
    -p PORT, --port PORT
        FROM 1 - 35535
        
    -m DOS_MODE, --mode DOS_MODE
        [tcp / udp / tor]
        
    -a AMOUNT, --amount AMOUNT
        AMOUNT OF THREADS
        
    -bs BUFFER_SIZE, --buffer-size BUFFER_SIZE
        PACKET SIZE IN BYTES FROM 1 - 65507
        
+ If you use TOR then follow these Steps:
    + you must setup first your torrc to cookie authentication method (https://www.linux.com/tutorials/beginners-guide-tor-ubuntu/)
    + If course, TOR have to run on "localhost" and port "9050"    

+ TO EXIT DOS JUST PRESS CTRL + C 

##### MIT LICENSE
+ read LICENSE for futher information
+ Coded by PiereLucas (Julian Huch)
