import socket
import time
import threading

def one_send(sock_one,sock_two):
    while True:
        sock_one.send(sock_two.recv(1024))

def two_send(sock_one,sock_two):
    while True:
        sock_two.send(sock_one.recv(1024))


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s. bind(('127.0.0.1',9999))
    s.listen(5)
    n = 0
    print('Waitting for match!!')
    while True:
        sock,addr = s.accept()
        print('One client is connect successful,info',addr)
        n += 1
        if n == 1:
            sock.send(bytes('You are first man,Please waitting for other one !','utf-8'))
            sock_one = sock
            continue
        elif n == 2:
            print('Now Full man')
            sock_two = sock
            sock_one.send(bytes('People Match,Go','utf-8'))
            sock_two.send(bytes('People Match,Go', 'utf-8'))
            t1 = threading.Thread(target=one_send,args=((sock_one,sock_two)))
            t2 = threading.Thread(target=two_send,args=((sock_one,sock_two)))
            t1.start()
            t2.start()
        else:
            sock.send(bytes('Full people!','utf-8'))




