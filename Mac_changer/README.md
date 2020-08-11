# Mac_Changer:

  - Both the programs are to be run through command line (linux).

## simple_mac_changer:
  
  - use 'raw_input' instead of 'input' (line no 4 &  5) in order to
    use in Python2.
	
  - How to Run the program (through command line)? :
    <br/> Example:
<<<<<<< HEAD
	
=======
    
>>>>>>> 03acc2ccf98c01c78e9f09d90cdbbe45ecad24bb
	root@kali:~/PycharmProjects/Mac_changer# python3 simple_mac_changer.py 
	[Press Enter]
	
	root@kali:~/PycharmProjects/Mac_changer# 
	
	---The mac would have changed---
	
  ** Here 'Mac_changer' is project name and 'simple_mac_changer.py' is python file.
    
  ** Replace python3 with python when using python2 to change mac address.

	
## main_mac_changer:

  - This program is made with python2. In order to use it with Python3 
    just replace 'testing' with 'testing.decode()' (line no 28).
  
  - How to Run the program (through command line)? :
    <br/> Example:
  
    root@kali:~/PycharmProjects/Mac_changer# python mac_changer_main.py -i eth0 -m 40:22:44:43:54:24 
	[Press Enter]

    [+] Current Mac is: 40:22:44:43:54:23

    [+] Changing mac address for eth0 to 40:22:44:43:54:24

    [+] Mac address is successfully changed to 40:22:44:43:54:24

    root@kali:~/PycharmProjects/Mac_changer# 
	
  ** Here 'Mac_changer' is project name and 'main_mac_changer.py' is python file.
    
  ** Replace python with python3 when using python3 to change mac address.

Note: Dont misuse the program.
  
