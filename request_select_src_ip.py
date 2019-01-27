#-*- coding: utf-8 -*-

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3 import poolmanager


class SourceAddressAdapter(HTTPAdapter):
	def __init__(self, source_address, **kwargs):
		self.source_address = (source_address, 24)
		super(SourceAddressAdapter, self).__init__(**kwargs)

	def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
		self.poolmanager = poolmanager.PoolManager(
			num_pools=connections,
			maxsize=maxsize,
			block=block,
			source_address=self.source_address)

	def proxy_manager_for(self, proxy, **kwargs):
		kwargs['source_address'] = self.source_address
		return super(SourceAddressAdapter, self).proxy_manager_for(
			proxy, **kwargs)

def main(src_ip):
	s = requests.session()
	a = SourceAddressAdapter(src_ip)
	url = 'http://192.168.1.xx:5000/'
	s.mount('http://', a)
	res = s.get(url)
	print(res.status_code)
	print(res.text)


if __name__ == '__main__':
	main('192.168.1.1')


	
