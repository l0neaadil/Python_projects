## Steps to execute the program:

1. <ins> Become man-in-the-middle</ins>: In order to be a man-in-the-middle, you 
need to execute the ARP Spoofer.
 
2. <ins> Trapping all packets in a queue</ins>:
- For remote machine

		iptables -I FORWARD -j NFQUEUE --queue-num 0

OR 
- For local machine

	iptables -I OUTPUT -j NFQUEUE --queue-num 0

	iptables -I INPUT -j NFQUEUE --queue-num 0



3. <ins>Run Code_injector</ins>:

- To run injector.py use command in the form:
   
		root@kali:~/PycharmProjects/Code_injector# python injector.py
   
4. Don't forget to execute the following command after you are done with 
Code_injector.

		iptables --flush
   
### Note:

- Have a look at DNS Spoofer before using this program.
- The program is to be run through command line (linux).
- The program has been tested on python2.
- Dont misuse the program.
