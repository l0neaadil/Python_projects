# Packet Sniffer:

Sniffers are programs that can capture/sniff/detect network traffic 
packet by packet and analyse them for various reasons.

## Scapy:

- Scapy is a library supported by both Python2 and Python3. It is used
  for interacting with the packets on the network. It has several 
  functionalities through which we can easily forge and manipulate the 
  packet. Scapy module is not included in Python3 library by default.
  
### scapy.sniff(iface=interface, store=False, prn=function)

- sniff() function can capture/sniff/detect network traffic packet by 
  packet and analyse them for various reasons. Some of the Sniff() 
  function arguments are:
- iface: Sniff for packets only on the provided interface.
- store: Whether to store sniffed packets or discard them. When you 
  only want to monitor your network forever, set store to 0.
- prn: sniff has an argument prn that allows you to pass a function that
 executes with each packet sniffed. The intended purpose of this function
 is to control how the packet prints out in the console allowing you to 
 replace the default packet printing display with a format of your choice.
 
 ### Note:
- The program is to be run through command line (linux).
- The program has been tested on python2.

   
- To run sniffer.py use command in the form:
   
   '''
   root@kali:~/PycharmProjects/Packet_sniffer# python sniffer.py
   '''
  
- In order to use it on other machine first enable ARP_Spoofer and
  then run this program. 
- Dont misuse the program.