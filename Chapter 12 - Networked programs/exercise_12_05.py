# Exercise 5: (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv is
# receiving characters (newlines and all), not lines.

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

show = False
while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    text = data.decode()
    if show:
        print(text, end='')
        continue
    pos = text.find("\r\n\r\n")
    if pos >= 0:
        print(text[pos + 4:], end='')
        show = True

mysock.close()