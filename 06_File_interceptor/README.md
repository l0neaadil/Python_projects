## Steps to execute the program:

1. <ins> Become man-in-the-middle</ins>: In order to be a man-in-the-middle, you 
need to execute the ARP Spoofer.
 
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

.....The picture has been taken from zsecurity.org.....

3. <ins>Run File_interceptor</ins>:

- To run interceptor.py use command in the form:
   
		'''
		root@kali:~/PycharmProjects/File_interceptor# python interceptor.py
		'''
   
4. Don't forget to execute the following command after you are done with 
File_interceptor.

		'''
		iptables --flush
		'''
   
### Note:

- The program is to be run through command line (linux).
- The program has been tested on python2.
- Dont misuse the program.
