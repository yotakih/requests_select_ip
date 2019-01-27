#-*- coding: utf-8 -*-

import subprocess
import ipaddress
from scapy.all import *

interface_name = 'ローカル エリア接続'
base_addr = ipaddress.ip_address('192.168.1.1')
net_mask = '255.255.255.0'
count = 10

def send_ping(ip, timeout):
	pkt = IP(dst=ip)/ICMP()
	res = sr1(pkt, timeout=timeout, verbose=0)
	if res.__repr__() == 'None':
		return False
	return True

def check_ip():
	for i in range(count):
		check_ip = str(base_addr + i)
		if send_ping(check_ip, 0.5):
			print('{:<15} : exists'.format(str(base_addr + i)))
		else:
			print('{:<15} : not exists'.format(str(base_addr + i)))

def ip_add():
	command = 'netsh interface ip add address name="%s addr=%s mask=%s'
	for i in range(count):
		subprocess.call(
			command % (interface_name, str(base_addr + i), net_mask)
		)

def ip_del():
	command = 'netsh interface ip delete address name="%s addr=%s mask=%s'
	for i in range(count):
		subprocess.call(
			command % (interface_name, str(base_addr + i), net_mask)
		)

if __name__ == '__main__':
	print('strat')
	check_ip()
	#ip_add()
	#ip_del()
		
