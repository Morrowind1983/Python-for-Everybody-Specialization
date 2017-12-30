# Exercise 1: Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page. You can use split('/') to break the URL into
# its component parts so you can extract the host name for the socket connect
# call. Add error checking using try and except to handle the condition where
# the user enters an improperly formatted or non-existent URL.

import socket
import urllib.parse

url = input("Please enter a URL:")
o = urllib.parse.urlparse(url)
host = o.hostname
port = o.port
if host is None:
    print("Improperly formatted URL")
    exit()
if port is None:
    port = 80
    
print("host =", host)
print("port =", port)

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, port))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except Exception as e:
    print(e)
    exit()

while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    print(data.decode(),end='')

mysock.close()
