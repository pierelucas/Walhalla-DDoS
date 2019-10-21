#### Walhalla DDoS → A Simple Python DDoS Script

##### Usage:

    ./walhalla.py -h    # For Help
    
    ./walhalla.py [-h] [-t TARGET_ADDR] [-p PORT] [-m DOS_MODE] [-a AMOUNT]
                   [-bs BUFFER_SIZE]
    
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
    
+ -a Amount defines the number of Threads
+ -bs Buffer size defines the package in bytes

+ close dos loop with ctrl+c

##### MIT LICENSE
+ read LICENSE for futher information
+ Coded by PiereLucas (Julian Huch)
