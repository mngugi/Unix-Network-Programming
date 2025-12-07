import socket

API_KEY = "AIzaSyDYfKFPlsmMRCFDxR-nVEN2uMckW393DZQ"

path = "/maps/api/geocode/json?address=207+N+Defiance+St+Archbold+OH&key=%s" % API_KEY

request = (
    "GET %s HTTP/1.1\r\n"
    "Host: maps.googleapis.com\r\n"
    "Connection: close\r\n"
    "\r\n"
) % path

sock = socket.socket()
sock.connect(('maps.googleapis.com', 80))
sock.sendall(request.encode())

response = sock.recv(4096)
print(response.decode())
