from socket import *
import sys
import os

serverPort = 8081
bufferSize = 4096

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 2)
sock.bind(('', serverPort))
sock.listen(1)

print ('Server connected to: localhost:{}'.format(serverPort))

def get_filetype(file_ext):
	if (file_ext == '.txt'):
		return 'Content-Type: text/plain\r\n'
	elif (file_ext == '.png'):
		return 'Content-Type: image/png\r\n'
	elif (file_ext == '.html'):
		return 'Content-Type: text/html\r\n'

while True:
	con, addr = sock.accept()
	req = con.recv(bufferSize).decode('utf-8')
	line = req.split(' ')

	method = line[0]
	path = line[1]
	http_version = line[2].split('\r\n')[0]
	header = ''
	try:
		file_o = open('.' + path, 'rb')
		response = file_o.read()
		file_o.close()
		header = '{} 200 OK\r\n'.format(http_version)

		file_name, file_ext = os.path.splitext(path)

		file_type = get_filetype(file_ext)
		header += file_type

		final = header.encode('utf-8')
		final += '\r\n'.encode('utf-8')
		final += response
		final += "\r\n".encode('utf-8')

		con.sendto(final)
	except:
		header = 'HTTP/1.1 404 Not Found\n\n'
		response = "<html><body><center><h3>Error 404: File not found</h3></center></body></html>".encode('utf-8')
		final_response = header.encode('utf-8')
		final_response += response
		con.send(final_response)
	con.close()
