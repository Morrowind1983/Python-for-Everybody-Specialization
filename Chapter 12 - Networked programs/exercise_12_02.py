# Exercise 2: Change your socket program so that it counts the number of
# characters it has received and stops displaying any text after it has shown
# 3000 characters. The program should retrieve the entire document and count the
# total number of characters and display the count of the number of characters
# at the end of the document.

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

count = 0
while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    text = data.decode()
    count += len(text)
    if count > 3000:
        continue
    print(text,end='')

print("total number of characters:", count)

mysock.close()
