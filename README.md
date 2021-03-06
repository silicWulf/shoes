# shoes - because socks weren't enough

Shoes is a module for Python 3 that makes sockets easier for users, while retaining the normal sockets function.

## FAQ

### What is shoes?

Look up like three lines mate!

### Why should I use shoes?

You shouldn't, if you're experienced with sockets. This is a toned-down wrapper for sockets that is meant for new programmers. It provides a far easier interface for creating socket servers and clients.

An example of this being easier: let's say we wanted to make a server that sent a message "Hello!" to all the connected users every second. We need notice if the user is disconnected as well. Here's the code in the regular `socket` module:

```python
import time
import socket
import threading
sock=socket.socket()
sock.bind("0.0.0.0",11111)
sock.listen(0)
conns=[]
def listener():
	global conns
	while True:
		conn,addr=sock.accept()
		conns.append(conn)
thread1=threading.Thread(target=listener)
thread1.daemon=True
thread1.start()
while 1:
	time.sleep(1)
	for conn in conns:
		try:
			conn.send(bytes("Hello!",encoding='utf-8'))
		except:
			print("User has disconnected!")
```

...and here's the code in the `shoes` module:


```python
import time
import shoes
sock=shoes.Server("0.0.0.0",11111)
sock.listen()
while 1:
	time.sleep(1)
	sock.sendall("Hello!")
```

A pretty vast difference, huh? It takes up roughly 4x less space than vanilla `socket`.

If you are an experienced developer that doesn't really need the fancy/cool stuff from `socket` and just wants a minimalistic way to manage sockets then this module can support that want.

## Documentation

### shoes.Socket(ip,port)

A basic `Socket` class, used for connecting to servers.

 * `ip` -- *(str)* The IP address to connect to 
 * `port` -- *(int)* The port to connect through

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send(message)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends a message to the connected server.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `message` -- *(str)* The message to send to the server

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns decoded data from the server. This is also aliased as "recieve" because I don't know how to spell.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disconnect()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Disconnects from the server.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout(seconds)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sets the timeout for most socket functions to seconds `seconds`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `seconds` -- *(int)* The number of seconds that the timeout should be set to. Can also be `None` to set no timeout.


### shoes.Server(ip,port)

A basic `Server` class, used for starting a server. Note: the server must be listening in order to accept any connections.

 * `ip` -- *(str)* The IP address to bind the server to
 * `port` -- *(int)* The port to bind the server to

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send(conn,message)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends a message to the connected client.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `conn` -- *(socket.socket)* The connection socket to the client to send the message to

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `message` -- *(str)* The message to send to the client `conn`

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sendall(message)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends a message to all connected clients.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `message` -- *(str)* The message to send to the client `conn`

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive(conn)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns received data from a connected client. This is also aliased as "recieve" because I don't know how to spell.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `conn` -- *(socket.socket)* The connection socket to the client to send the message to

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Starts the listening of a server to accept connections. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INFO: Once listening and connections have been made between the server and client, `Server.user_count` and `Server.connections` become non-zero/non-None.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stoplisten()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stops the listening of a server to accept connections. Note: connections that have already been made will not be terminated.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;autorefresh()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This function starts updating the `user_count` and `connections` as much as possible, not just when an attempt to send or receieve from a connection is made. NOTE: THIS PRODUCES ERRORS IF THE CLIENT IS NOT USING THIS MODULE! This is because in order to keep the connections updated, it needs to send a character that can cause errors with programs that listen and interpret every single thing sent to it.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout(seconds)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sets the timeout for most socket functions to seconds `seconds`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * `seconds` -- *(int)* The number of seconds that the timeout should be set to. Can also be `None` to set no timeout.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connections
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(list(tuple(`socket.socket`, tuple(str, int))))* (jeez that was a mouthful) A list of tuples containing a connection `socket.socket` and another tuple containing the IP address and port of the client.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_count
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(int)* An `int` of how many users are connected.
