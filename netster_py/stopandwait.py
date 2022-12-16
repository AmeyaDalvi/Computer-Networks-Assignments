from typing import BinaryIO
import socket
# import time


def udp_server(iface, port, fp):
    print("Hello, I am a server")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_port = socket.getaddrinfo(iface, port, socket.AF_INET, socket.SOCK_DGRAM)
    host_port = host_port[0][4]
    s.bind(host_port)
    rudp_header = '0'

    while True:
        data = s.recvfrom(256)
        client_ack = data[0][0]
        decoded_client_ack = client_ack.decode('utf-8')
        message = data[0][1:]
        if not message:
            s.sendto(str.encode('finish'), data[1])
            break

        if rudp_header == decoded_client_ack:
            s.sendto(str.encode(rudp_header), data[1])
            
        else:
            fp.write(message)
            rudp_header = decoded_client_ack
            s.sendto(str.encode(rudp_header), data[1])
    
    fp.close()
    s.close()


def udp_client(host, port, fp):
    print("Hello, I am a client")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    host_port = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_DGRAM)
    host_port = host_port[0][4]
    s.connect(host_port)
    s.settimeout(0.2)
    alt_bit = '1'

    while True:
        client_message = alt_bit.encode() + fp.read(255)
        s.sendto(client_message, host_port)

        if not client_message:
            break

        while True:
            try:
                data = s.recvfrom(256)
                ack = data[0]
                decoded_ack = ack.decode('utf-8')
                
                if decoded_ack == 'finish':
                    break

                if decoded_ack == alt_bit:
                    if decoded_ack == '0':
                        alt_bit = '1'
                    else:
                        alt_bit = '0'
                    break
        
            except socket.error as socketerror:
                s.sendto(client_message, host_port)

        if decoded_ack == 'finish':
            break

    fp.close()
    s.close()


def stopandwait_server(iface: str, port: int, fp: BinaryIO) -> None:
    if iface is None:
        iface = '0.0.0.0'
    udp_server(iface, port, fp)

def stopandwait_client(host: str, port: int, fp: BinaryIO) -> None:
    udp_client(host, port, fp)
