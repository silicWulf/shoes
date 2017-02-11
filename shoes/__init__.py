import os
import sys
import socket
import warnings
import threading

class Socket:
	def __init__(self,ip,port):
		self.ip = ip
		self.port = port
		self.sock = socket.socket()
		self.sock.bind((self.ip, self.port))
	def send(self,message):
		try:
			self.sock.send(bytes(message, encoding='utf-8'))
		except:
			self.user_count -= 1
			self.connections.remove(conn)
			warnings.warn("Warning: connection tunnel has been broken. User has disconnected.")
	def recieve(self):
		return self.sock.recv(4096).decode()


class Server:
	def __init__(self,ip,port,user_count=0,connections=[]):
		self.ip = ip
		self.port = port
		self.user_count = user_count
		self.connections = connections
		self.sock = socket.socket()
		self.stoplistening = 0
		self.nowstopped = 0
		self.sock.bind((self.ip, self.port))
	def send(self,conn,message):
		try:
			conn.send(bytes(message, encoding='utf-8'))
		except:
			self.user_count -= 1
			self.connections.remove(conn)
			warnings.warn("Warning: connection tunnel has been broken. User has disconnected.")
	def recieve(self,conn):
		return conn.recv(4096).decode()
	def listen(self):
		if self.listenthread:
			raise ListenThreadActive("a listen thread is already active")
		else:
			self.listenthread = threading.Thread(target = self._listendaemon, args = ())
			self.listenthread.daemon = True
			self.listenthread.start()
	def stoplisten(self):
		self.stoplistening = 1
		while self.nowstopped == 0:
			pass
		self.stoplistening = 0
		self.nowstopped = 0
		self.listenthread.join()
	def _listendaemon(self):
		self.sock.listen(255)
		while True:
			if self.stoplistening == 0:
				conn, addr = self.sock.accept()
				self.connections.append(conn)
				self.user_count += 1
			else:
				break
class ListenThreadActive(Exception):
	def __init__(self, message):
		self.message = message