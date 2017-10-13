import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))

s.listen(5)
while True:
	c, addr = s.accept()
	print 'link address:',addr
	while True:
	c.send('welcome browse !!!')
	;c.close()