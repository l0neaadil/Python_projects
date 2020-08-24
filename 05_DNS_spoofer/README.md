# DNS Spoofer:
DNS spoofing is a form of computer security hacking in which corrupt 
Domain Name System data is introduced into the DNS resolver's cache, 
causing the name server to return an incorrect result record.

### Steps to execute the program:

1. <ins> Man-in-the-Middle</ins>: In order to be a man-in-the-middle, you 
need to execute the ARP Spoofer, so the victim will be sending the 
DNS requests to your machine first, instead of directly routing them
into the Internet.
 
2. <ins> Trapping all packets in a queue</ins>:

		''' 
		iptables -I FORWARD -j NFQUEUE --queue-num 0
		'''

OR 

	''' 
	iptables -I OUTPUT -j NFQUEUE --queue-num 0

	iptables -I INPUT -j NFQUEUE --queue-num 0
	'''

This rule indicates that whenever a packet is forwarded, redirect it 
( -j for jump ) to the netfilterqueue number 0. This will enable us 
to redirect all the forwarded packets into Python. 

![iptables](https://user-images.githubusercontent.com/68290275/90950646-39c6f900-e471-11ea-8e44-27c3175a433f.jpg)


3. <ins>Run DNS_Spoofer</ins>:

- To run spoofer.py use command in the form:
   
		'''
		root@kali:~/PycharmProjects/DNS_spoofer# python spoofer.py
		'''
   
4. Don't forget to execute the following command after you are done with 
DNS_Spoofer.

		'''
		iptables --flush
		'''
   
### Note:
- <ins>netfilterqueue</ins>: For accessing and modifying packets we use netfilterqueue. Whenever
a new packet is redirected to the netfilterqueue, a function (in our
case 'process_packet') is called.

![netfilterqueue](https://user-images.githubusercontent.com/68290275/90950784-9a0a6a80-e472-11ea-85d5-c1c41a3dd09e.jpg)


- <ins>get_payload()</ins> shows actual contents inside a packet and <ins>scapy.IP()</ins> converts netfilterqueue packet
to scapy packet.
- <ins>packet.accept()</ins> will forward the packet to its destination while <ins>packet.drop()</ins>
 drops them and does not forward them.
 
- The program is to be run through command line (linux).
- The program has been tested on python2.
- Dont misuse the program.
