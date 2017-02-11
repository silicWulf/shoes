# shoes - because socks weren't enough

Shoes is a module for Python 3 that makes sockets easier for users, while retaining the normal sockets function.

## Documentation

### shoes.Socket(ip,port)

A basic `Socket` class, used for connecting to servers.

* `ip` -- *(str)* The IP address to connect to 
* `port` -- *(int)* The port to connect through

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send(message)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends a message to the connected server.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* `message` -- *(str)* The message to send to the server

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recieve()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns decoded data from the server.

### shoes.Server(ip,port)

A basic `Server` class, used for starting a server. Note: the server must be listening in order to accept any connections.

* `ip` -- *(str)* The IP address to bind the server to
* `port` -- *(int)* The port to bind the server to

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send(conn,message)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends a message to the connected client.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* `conn` -- *(socket.socket)* The connection socket to the client to send the message to
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* `message` -- *(str)* The message to send to the client `conn`

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recieve(conn)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recieves data from a connected client.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* `conn` -- *(socket.socket)* The connection socket to the client to send the message to

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Starts the listening of a server to accept connections. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INFO: Once listening and connections have been made between the server and client, `Server.user_count` and `Server.connections` become non-zero/None.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stoplisten()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stops the listening of a server to accept connections. Note: connections that have already been made will not be terminated.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connections
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(list)* A list of connections `socket.socket`.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_count
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(int)* An `int` of how many users are connected.
