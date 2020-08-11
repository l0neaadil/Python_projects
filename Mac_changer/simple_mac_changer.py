#!/usr/bin/env python
import subprocess

interface = input('enter the name of interface ---> ')
mac = input('enter mac address ---> ')

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
subprocess.call(['ifconfig', interface, 'up'])

