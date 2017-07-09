import socket;
s = socket.socket();
host = socket.gethostname();
port = 14439
s.connect(("184.191.64.88", port))
if (s.recv(1024) == b"good"):
    s.send(str.encode(input()))
strg = s.recv(1024)
print(strg)
s.close()