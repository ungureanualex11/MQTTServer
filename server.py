import socket
# crearea unui socket de tip IPV4, TCP
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#crearea unui obiect care stocheaza numele host-ului
host='127.0.0.1'

#definirea unui port unde ne dorim sa cream serverul
port=5000

#asocierea la server a adresei(host+port) 
serversocket.bind( (host,port) )
