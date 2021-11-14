# Mac_Changer:

  - Program for changing mac address.
  
## Plan:

 Step 1: To give input (interface name and new mac address) through terminal.{optparse module}
 
 Step 2: Checking old mac address (the mac address which we will change).{subprocess + re module}
 
 Step 3: Changing mac address. {subprocess module}
 
 Step 4: Checking for new mac address. 

## simple_mac_changer:
  
  - use 'raw_input' instead of 'input' (line no 4 &  5) in order to
    use in Python2.
	
  - How to Run the program (through command line)? :
    <br/> Example:

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

### Hints and Tips:

 - Shebang specifies which program should be called to run the script.
 
		#! interpreter_path
 - parse_args() method of OptionParser returns tuple ({},[]) containing a dictionary and a list.
 - subprocess module is used for accessing system commands. 
 - optparse module is used for giving input through terminal.
 - re module is used for searching a pattern from a string.
 - To get an overview of ifconfig command click on the link:
 
   https://loneaadil.medium.com/a-brief-overview-of-ifconfig-command-d56a7765106
 
### Note: 
 - Both the programs are to be run through command line (linux).
 
 - Dont misuse the program.
  
