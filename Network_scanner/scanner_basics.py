# ARP packet and Ethernet packet
import scapy.all as scapy


def scan(ip):
    arp_packet = scapy.ARP()
    arp_packet.show()

    Ethernet_packet = scapy.Ether()
    Ethernet_packet.show()

    arp_packet = scapy.ARP(pdst=ip)
    print(arp_packet.summary())
    arp_packet.show()

    Ethernet_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:bb')
    print(Ethernet_packet.summary())
    Ethernet_packet.show()


scan('10.0.2.3')
