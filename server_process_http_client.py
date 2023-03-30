from socket import *
import socket
import threading
import time
import sys
import logging
from http import HttpServer

def ProcessClientRequest(connection, addr):
		httpserver = HttpServer()
		rcv=""
		while True:
			try:
				data = connection.recv(32)
				if data:
					logging.warning("Connected %r at %r", connection, addr)
					#merubah input dari socket (berupa bytes) ke dalam string
					#agar bisa mendeteksi \r\n
					d = data.decode()
					rcv=rcv+d
					if rcv[-2:]=='\r\n':
						#end of command, proses string
						logging.warning("data dari client: {}" . format(rcv))
						hasil = httpserver.proses(rcv)
						#hasil akan berupa bytes
						#untuk bisa ditambahi dengan string, maka string harus di encode
						hasil=hasil+"\r\n\r\n".encode()
						logging.warning("balas ke  client: {}" . format(hasil))
						#hasil sudah dalam bentuk bytes
						connection.sendall(hasil)
						rcv=""
						connection.close()
				else:
					break
			except OSError as e:
				pass
		connection.close()