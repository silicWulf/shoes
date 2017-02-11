import os
import sys
import socket
import warnings
import threading

class Socket:
	def __init__(self,ip,port):
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.ip, self.port))
	def send(self,message):
		try:
			self.sock.send(bytes(message, encoding='utf-8'))
		except:
			self.user_count -= 1
			self.connections.remove(conn)
			warnings.warn("Warning: connection tunnel has been broken. Disconnected from server.")
	def receive(self):
		try:
			return self.sock.recv(4096).decode()
		else:
			warnings.warn("Warning: connection tunnel has been broken. Disconnected from server.")
			return None
	def recieve(self,conn):
		return self.receive(conn)
	def disconnect(self):
		self.sock.disconnect()


class Server:
	def __init__(self,ip,port):
		self.ip = ip
		self.port = port
		self.user_count = 0
		self.connections = []
		self.sock = socket.socket()
		self.stoplistening = 0
		self.nowstopped = 0
		self.listenthread = None
		self.sock.bind((self.ip, self.port))
	def send(self,conn,message):
		try:
			conn.send(bytes(message, encoding='utf-8'))
		except:
			self.connections.remove(conn)
			self.user_count = len(self.connections)
			warnings.warn("Warning: connection tunnel has been broken. User has disconnected.")
	def sendall(self,message):
		for conn, addr in self.connections:
			try:
				self.send(conn, message)
			except:
				self.connections.remove(conn)
				self.user_count = len(self.connections)
				warnings.warn("Warning: connection tunnel for " + addr[0] + " has been broken. User has disconnected.")
	def receive(self,conn):
		try:
			return conn.recv(4096).decode()
		else:
			warnings.warn("Warning: connection tunnel has been broken. User has disconnected.")
			return None
	def recieve(self,conn):
		return self.receive(conn)
	def listen(self):
		try:
			self.listenthread = threading.Thread(target = self._listendaemon, args = ())
			self.listenthread.daemon = True
			self.listenthread.start()
		except:
			raise ListenThreadActive("a listen thread is already active")
			
	def stoplisten(self):
		self.stoplistening = 1
		while self.nowstopped == 0:
			pass
		self.stoplistening = 0
		self.nowstopped = 0
		self.listenthread.join()
	def _listendaemon(self):
		self.sock.listen(0)
		while True:
			if self.stoplistening == 0:
				conn, addr = self.sock.accept()
				if self.stoplistening == 0:
					pass
				else:
					self.connections.append((conn, addr))
					self.user_count = len(self.connections)
			else:
				break
class ListenThreadActive(Exception):
	def __init__(self, message):
		self.message = message