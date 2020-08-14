#!/usr/bin/env python
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='type -i eth0')
    parser.add_option('-m', '--mac', dest='mac', help='type -m 00:11:22:33:44:55')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface. Use --help for more info")
    elif not options.mac:
        parser.error("[-] Please specify mac. Use --help for more info")
    return options


def change_mac(interface, mac):
    print("[+] Changing mac address for " + interface + " to " + mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])


def get_mac(interface):
    testing = subprocess.check_output(['ifconfig', interface])
    mac_addr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", testing)
    if mac_addr:
        return mac_addr.group(0)
    else:
        print("mac address not found")


option = get_arguments()
mak = get_mac(option.interface)
print("\n[+] Current Mac is: " + str(mak))
change_mac(option.interface, option.mac)
mak = get_mac(option.interface)
if mak == option.mac:
    print("[+] Mac address is successfully changed to " + mak + '\n')
else:
    print("Mac address did not get changed \n")

