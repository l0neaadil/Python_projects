# Backdoor:
A backdoor is a means to access a computer system or encrypted data in order to bypass the 
system's customary security mechanisms. A developer may create a backdoor so that an
application or operating system can be accessed for troubleshooting or other purposes. 
However, attackers often use backdoors that they detect or install themselves as part 
of an exploit. Whether installed as an administrative tool, a means of attack 
or as a mechanism allowing the government to access encrypted data, a backdoor is a security 
risk because there are always threat actors looking for any vulnerability to exploit.

## socket:
A socket is one endpoint of a two-way communication link between two machines on a network. 
An endpoint is a combination of an IP address and a port number. One socket listens on a particular 
port at an IP, while other socket reaches out to that socket to form a connection. 
Server forms the listener socket while client reaches out to the server. 
To create a socket, you must use the socket.socket() function available in socket module, which has the general syntax:

        s = socket.socket (socket_family, socket_type)
		
socket_family represents the family of protocols that is used as the transport mechanism.
socket_type represents the type of communications between the two endpoints, typically 
SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.

### Server Socket Methods:
Initially  <ins>bind()</ins> method is used by the server which binds a socket to a specific ip and port. Then the server uses 
<ins>listen()</ins> method which puts the server into listen mode. This allows the server to listen 
to incoming connections. The server then uses accept() and close() method. The <ins>accept()</ins>
method initiates a connection with the client and the <ins>close()</ins> method closes the connection 
with the client.

### Client Socket Methods:
The client uses <ins>connect()</ins> method in order to connect with the server.

### General Socket Methods:

![1socket](https://user-images.githubusercontent.com/68290275/119869496-ef156880-bf3d-11eb-828d-73fc0674fa83.png)

- <ins>recv()</ins>: This method receives TCP message.
- <ins>send()</ins>: This method transmits TCP message.
- <ins>close()</ins>: This method closes socket.	

![3socket](https://user-images.githubusercontent.com/68290275/119867736-d7d57b80-bf3b-11eb-9c70-a6ce9cf92866.png)

## JSON:
JSON is a syntax for storing and exchanging data. Python has a built-in 
package called json, which can be used to work with JSON data. 
- Conversion from JSON to Python: If you have a JSON string, you can parse it by 
using the <ins>json.loads()</ins> method.
- Conversion from Python to JSON: If you have a Python object, you can convert it 
into a JSON string by using the <ins>json.dumps()</ins> method.

### Note:
- The program has been tested using python3 on windows machine.
- Dont misuse the program.
