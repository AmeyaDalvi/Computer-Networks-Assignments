
'''
Name: Ameya Dalvi
mail: abdalvi@iu.edu

Sockets using Python and netster

Refered Links :

https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
https://pythontic.com/modules/socket/udp-client-server-example

For multi-threading:
https://docs.python.org/3/library/_thread.html
https://www.geeksforgeeks.org/socket-programming-multi-threading-python/

Sockets:

For sockets creation I have used python's inbuilt Socket module. We create a socket for a IPV4 tcp connection
and then bind the socket to the host and port supplied. The server/client is then set on a listening mode.


Server: 

I have implemented the multi-threaded tcp server using Python's _thread API.
The socket's accept function accepts a tcp connection from a client on a loop and 
return the connection and client's address.

For UDP as it is connectionless, it doesn't really need to actively keep listening and hence we do
not need to call to explicitly call the accept function.

start_new_thread(): takes in a function for starting a new server thread each time a new client request
for a connection.

Client:

The client function is pretty straight forward, we create a socket and connect to the the server.


'''

import socket
from _thread import *


def threaded(conn,s):
    while True:
        client_message = conn.recv(2048)
        if not client_message:
            break
        client_message_decoded = client_message.decode("utf-8")
        if client_message_decoded[-1]== '\n':
            client_message_decoded = client_message_decoded.replace("\n", "")
        if client_message_decoded == 'hello':
            client_message_decoded = 'world\n'
        elif client_message_decoded == 'goodbye':
            client_message_decoded = 'farewell\n'
            conn.send(client_message_decoded.encode("utf-8"))
            conn.close()
            break
        elif client_message_decoded == "exit":
            client_message_decoded = 'ok\n'
            conn.send(client_message_decoded.encode("utf-8"))
            conn.close()
            break
        if client_message_decoded[-1]!= '\n':
            client_message_decoded += "\n"
        conn.send(client_message_decoded.encode("utf-8"))
    if client_message_decoded == "ok\n":
        s.shutdown(socket.SHUT_RDWR)
        s.close()


def tcp_server(iface, port):
    print("Hello, I am a server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, )
    host_port = socket.getaddrinfo(iface, port);
    host_port = host_port[0][4]
    s.bind(host_port)
    s.listen(5)
    # s.setblocking(False)
    while True:
        # print("ready to accept")
        try:
            conn, addr = s.accept()
            print(f"connection from ('{addr[0]}',{addr[1]})")
            start_new_thread(threaded, (conn,s))
        except Exception as e:
            s.close()
            # print("closing server socket")
            break
    

def tcp_client(host, port):
    print("Hello, I am a client")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host_port = socket.getaddrinfo(host, port);
    host_port = host_port[0][4]
    s.connect(host_port)
    while True:
        message = input()
        if message[-1]!= '\n':
            message += "\n"
        s.send(message.encode("utf-8"))

        data = s.recv(2048).decode("utf-8")
        data = data.rstrip('\n')
        print(data)
        if data == 'ok'.rstrip('\n') or data == 'farewell'.rstrip('\n'):
            break
    s.close()


def udp_server(iface, port):
    print("Hello, I am a server")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_port = socket.getaddrinfo(iface, port, socket.AF_INET, socket.SOCK_DGRAM)
    host_port = host_port[0][4]
    print(host_port)
    s.bind(host_port)
# 
    
    while True:
        data = s.recvfrom(2048)
        if not data[0]:
            break
        client_message_decoded = data[0].decode("utf-8")
        if "\n" in client_message_decoded:
            client_message_decoded = client_message_decoded.replace("\n", "")
        if client_message_decoded == 'hello':
            client_message_decoded = 'world\n'
        elif client_message_decoded == 'goodbye':
            client_message_decoded = 'farewell\n'
        elif client_message_decoded == "exit":
            client_message_decoded = 'ok\n'
            s.sendto(str.encode(client_message_decoded), data[1])
            break
        if client_message_decoded[-1]!= '\n':
            client_message_decoded += "\n"
        s.sendto(str.encode(client_message_decoded), data[1])

    

def udp_client(host, port):
    print("Hello, I am a client")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    host_port = ''
    for fa, ty, flags, _, addr in socket.getaddrinfo(host,port, socket.AF_INET, socket.SOCK_STREAM):
        host_port = addr
    # host_port = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_DGRAM)
    # host_port = host_port[0][4]
    print(host_port)
    s.connect(host_port)
    while True:
        message = input()
        if message[-1]!= '\n':
            message += "\n"
        s.sendto(str.encode(message), (host, port))
        data = s.recvfrom(2048)
        print(data[0].decode("utf-8").rstrip('\n'))
        if data[0].decode("utf-8").rstrip('\n') == 'ok' or data[0].decode("utf-8").rstrip('\n') == 'farewell':
            break
    s.close()


def chat_server(iface:str, port:int, use_udp:bool) -> None:
    if use_udp == 0:
        tcp_server(iface, port)
    else:
        udp_server(iface, port)


def chat_client(host:str, port:int, use_udp:bool) -> None:
    if use_udp == 0:
        tcp_client(host, port)
    else:
        udp_client(host, port)


