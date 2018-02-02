import socket
import time
import threading


def tcpsend(s):
    while True:
        s.send(bytes(input('>>>'),'utf-8'))

def tcprecv(s):
    while True:
        print(str(s.recv(1024),'utf-8'))


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))
    join_in_text = str(s.recv(1024),'utf-8')
    if join_in_text == 'Full people!':
        print('Now Full People, you can join in!')
        print('Perpare to close!!')
        s.close()
    else:
        print(join_in_text)
        t1 = threading.Thread(target=tcpsend,args=((s,)))
        t2 = threading.Thread(target=tcprecv, args=((s,)))
        t1.start()
        t2.start()
