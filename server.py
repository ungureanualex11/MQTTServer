import socket
# crearea unui socket de tip IPV4, TCP
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#crearea unui obiect care stocheaza numele host-ului
host='127.0.0.1'

#definirea unui port unde ne dorim sa cream serverul
port=5000

#asocierea la server a adresei(host+port) 
serversocket.bind( (host,port) )

#crearea unui listener TCP, parametrul fiind numarul de conexiuni alocate
serversocket.listen(3)

while True:
    #realizam conexiunea
    clientsocket,address = serversocket.accept()

    print("Conexiune primita de la " % str(address))
    
    #Mesajul trimis clientului in cazul conectarii cu succes
    message = 'Salut! Iti multumim ca te-ai conectat la serverun nostru' + "\r\n"
    
    clientsocket.send(message)

    clientsocket.close()
