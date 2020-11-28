# Packet Sniffer:

Sniffers are programs that can capture/sniff/detect network traffic 
packet by packet and analyse them for various reasons.

# Plan:
As for introductory purpose here we are sniffing HTTP Request packets only.
- Start sniffing by using scapy's sniff() function.
- Get url of all sites which are called when we click on a link.
- Get username and password if it is entered.

## Scapy:

- Scapy is a library supported by both Python2 and Python3. It is used
  for interacting with the packets on the network. It has several 
  functionalities through which we can easily forge and manipulate the 
  packet. Scapy module is not included in Python3 library by default.
  
- summary(): This method provide us the status of the packet that we
 have created. It does not provide the detailed information about the 
 packet, it just gives us the basic idea like what is the destination 
 of the packet etc.

- show(): This method is very similar to summary() method. It gives
 more detailed information about the packet.

- ARP(): This function defined in scapy module allows us to create 
ARP packets (request or response). By default, if we are calling it, 
it will create an ARP request packet for us. 

- Send/Receive Functions: Scapy comes with send(), sendp(), sr(), srp(),
sr1() and srp1() functions for sending packets and receiving responses.
The send() functions are used to send  packets while sr() functions are
used to send  packets when you expect a response back. The p at the end 
of the function name means that we're sending at L2 instead of L3. The 
functions with a 1 in them mean that Scapy will send the specified packet
and end after receiving 1 answer/response instead of continuing to listen
for answers/responses.

- sniff(): sniff() function can capture/sniff/detect network traffic packet by 
  packet and analyse them for various reasons. Some of the Sniff() 
  function arguments are:
	- iface: Sniff for packets only on the provided interface.
	- store: Whether to store sniffed packets or discard them. When you 
             only want to monitor your network forever, set store to 0.
	- prn: sniff has an argument prn that allows you to pass a function that
           executes with each packet sniffed. The intended purpose of this function
           is to control how the packet prints out in the console allowing you to 
		   replace the default packet printing with a format of your choice.
		   
  
			scapy.sniff(iface=interface, store=False, prn=callback_function)

 
 
 ### Note:
- The program is to be run through command line (linux).
- The program has been tested on python2.
   
- To run sniffer.py use command in the form:
   
   root@kali:~/PycharmProjects/Packet_sniffer# python sniffer.py
  
- In order to use it on other machine first enable ARP_Spoofer and
  then run this program. 
- URL on which you can test this program:

http://testphp.vulnweb.com/login.php
	
- Dont misuse the program.