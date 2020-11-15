#!/usr/bin/env python

import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='ip', help='enter ip/ip range')
    option, arguments = parser.parse_args()
    return option


def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    ethernet_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ethernet_packet/arp_packet
    answered_list = scapy.srp(packet, timeout=3, verbose=False)[0]
    # For remembering purpose we can say that scapy.srp() returns tuple
    # with elements being answered_list and unanswered_list and the answered_list
    # which we are going to deal with contains more fields
    # ([({}, {}), ({}, {}), ({}, {})], [])

    client_list = []
    for element in answered_list:
        client_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def result(client_list):
    print('''____________________________________
    ip             mac
....................................''')
    for client in client_list:
        print(' ' + client['ip']+'   ' + client['mac'])


print('\n')

option = get_arguments()
client_list = scan(option.ip)
result(client_list)

print('\n')
