#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import re
import sys
def check_server(address, port):
	# Create a TCP socket
	s = socket.socket()
	try:
		s.connect((address, port))
		return True
	except socket.error as e:
		print (e)
		return False

if __name__ == '__main__':
	from optparse import OptionParser
	parser = OptionParser()
	
	parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")
	
	parser.add_option("-p", "--port", dest="port", type="int", default=80, help="PORT for server", metavar="PORT")
	
	(options, args) = parser.parse_args()
	check = check_server(options.address, options.port)	
	sys.exit(not check)
