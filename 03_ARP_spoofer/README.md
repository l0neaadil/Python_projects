# ARP Spoofer:

- ARP spoofing is a malicious attack in which the hacker sends falsified
ARP in a network. To design a python script to create an ARP spoofer, we 
require the scapy module which is a very powerful packet manipulation tool.

![basic network](https://user-images.githubusercontent.com/68290275/90243271-349ff380-de4c-11ea-8e03-3d1fd2263d60.jpg) 
![spoofed network](https://user-images.githubusercontent.com/68290275/90243729-0a026a80-de4d-11ea-965f-ce08a17a422e.jpg)
................These pictures have been taken from zsecurity.org..............


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

# Steps to create ARP Spoofer:

- Get the MAC address of the IP that we want to spoof.
- Then create a spoofing packet using the ARP() function to set the 
  target IP, Spoof IP and MAC address that we found above.
- Start the spoofing.
- Display the information of the numbers of packets sent.
- Finally, re-set the ARP tables of the spoofed address to defaults 
  after spoofing.
  
### Note:
- The program is to be run through command line (linux).
- The program has been tested on python2.

   
- To run spoofer.py use command in the form:
   
   '''
   root@kali:~/PycharmProjects/ARP_spoofer# python spoofer.py
   '''
   
- The following command is to be run in order to enable ip forwarding
so that the packet can flow through hackers computer without dropping 
and hacker can act as man in the middle.  

		'''
        echo 1 > /proc/sys/net/ipv4/ip_forward.
		'''

- Dont misuse the program.
