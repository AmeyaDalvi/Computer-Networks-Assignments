from typing import BinaryIO
import socket, time

def udp_server(iface, port, fp):
    print("Hello, I am a server")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_port = socket.getaddrinfo(iface, port, socket.AF_INET, socket.SOCK_DGRAM)
    host_port = host_port[0][4]
    s.bind(host_port)
    s.setblocking(False)

    next_seq = 0

    while True:
        try:
            data = s.recvfrom(256)
            client_ack = data[0][0:3]
            print(f"recv ack ==>{client_ack}")
            decoded_client_ack = client_ack.decode('utf-8')
            decoded_client_ack = decoded_client_ack.lstrip('#')
            message = data[0][3:]

            print(decoded_client_ack)
            if int(decoded_client_ack) == next_seq:
                if not message:
                    s.sendto(str.encode('finish'), data[1])
                    break
            
                else:
                    fp.write(message)
                    s.sendto(str(next_seq).encode("utf-8"), data[1])
                    next_seq += 1
            else:
                s.sendto(str(next_seq-1).encode("utf-8"), data[1])

        except socket.error as socketerror:
            pass


    
    fp.close()
    s.close()


def udp_client(host, port, fp):
    print("Hello, I am a client")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    host_port = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_DGRAM)
    host_port = host_port[0][4]
    s.connect(host_port)
    s.setblocking(0)
    send_base = 0
    next_seq = 0
    N = 128
    t0 = 0
    stop_timer = False

    while True:

        if next_seq < send_base + N:
            fp.seek(next_seq*253, 0)
            if next_seq < 10:
                str_next_seq = '##'+str(next_seq)
            elif next_seq < 100:
                str_next_seq = '#'+str(next_seq)
            else:
                str_next_seq = str(next_seq)

            client_message = str_next_seq.encode("utf-8") + fp.read(253)


            print("sending packet:",next_seq)
            s.sendto(client_message, host_port)


            if send_base == next_seq:
                t0 = time.time()

            next_seq += 1
        
        try:
            data = s.recvfrom(253)
            ack = data[0]
            decoded_ack = ack.decode('utf-8')

            print("decoded_ack", decoded_ack)
            print("next_seq", next_seq)

            if decoded_ack == 'finish':
                break
            
            send_base = int(decoded_ack) + 1
            print("send_base after first if",send_base)
            if send_base == next_seq:
                stop_timer = True
            else:
                t0 = time.time()
                stop_timer = False
            
        except socket.error as socketerror:
            pass

        if not stop_timer and time.time() - t0 >= 0.06:
            print("Timeout")
          
            t0 = time.time()
            print("send_base after timeout",send_base)
            start = send_base
            while start <= next_seq - 1:
                fp.seek(start*253)
                if start < 10:
                    str_start = '##'+str(start)
                elif start < 100:
                    str_start = '#'+str(start)
                else:
                    str_start = str(start)
                client_message = str_start.encode("utf-8") + fp.read(253)

                print("sending packet:",start)
                s.sendto(client_message, host_port)
                start+=1


def gbn_server(iface:str, port:int, fp:BinaryIO) -> None:
    if iface is None:
        iface = '0.0.0.0'
    udp_server(iface, port, fp)

def gbn_client(host:str, port:int, fp:BinaryIO) -> None:
    udp_client(host, port, fp)
