# ARP Spoofer:

- ARP spoofing is a malicious attack in which the hacker sends falsified
ARP in a network. To design a python script to create an ARP spoofer, we 
require the scapy module which is a very powerful packet manipulation tool.

![basic network](https://user-images.githubusercontent.com/68290275/90243271-349ff380-de4c-11ea-8e03-3d1fd2263d60.jpg) 
![spoofed network](https://user-images.githubusercontent.com/68290275/90243729-0a026a80-de4d-11ea-965f-ce08a17a422e.jpg)
These pictures have been taken from zsecurity.org.

# Steps to create ARP Spoofer:

- Find the mac address of target.
- Create ARP response packet having 
    - destination mac & destination ip of target,  
	- source ip of gateway  and 
    - source mac of hacker machine.
- Send ARP response packet to target.
- Similarly send ARP response packet to gateway with 
	- destination mac & destination ip of gateway,  
	- source ip of target  and 
    - source mac of hacker machine.
- Finally, after spoofing re-set the ARP tables of the spoofed addresses to defaults
  by creating and sending ARP packets having source macs of actual machines. 


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

   
- To run spoofer.py use command in the form:
   
	root@kali:~/PycharmProjects/ARP_spoofer# python spoofer.py

- The following command is to be run in order to enable ip forwarding
so that the packet can flow through hackers computer without dropping 
and hacker can act as man in the middle.  

        echo 1 > /proc/sys/net/ipv4/ip_forward.

- Dont misuse the program.
