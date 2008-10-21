#!/usr/bin/python

import os
import time
from scipy import io as matio
from twisted.internet import reactor
from twisted.web import soap,resource,server

mat2py_xcp = "/tmp/mat2py_xcp.mat"


class Mat2Py(soap.SOAPPublisher):
	def __init__(self):
		soap.SOAPPublisher()
		self.funcs = {}
		
	def reg_func(self, name, func):
		self.funcs[name] = func

	def soap_call(self, name):
		mat = matio.loadmat(mat2py_xcp)
		args = list( mat['varargin'] )
		try:
			func = self.funcs[name]
			ret = func( *args )
		except:
			print "Could not call %s with args [%s]", (name, args)
		d = {}
		if isinstance(ret, tuple):
			for i in range(len(ret)):
				d["ret%d"%(i+1)] = ret[i] 
		else:
			d["ret1"] = ret
		matio.savemat(mat2py_xcp, d)

if __name__ == '__main__':
	import sys

	def ping():
		time.sleep(3)
		print "ping() called"

	def hello(a, b):
		print "Hello!"
		print "  a=", a
		print "  b=", b
		return a,b,a*b

	m2p = Mat2Py()
	m2p.reg_func("ping", ping)
	m2p.reg_func("hello", hello)

	root = resource.Resource()
	root.putChild('mat2py', m2p )
	reactor.listenTCP(8080, server.Site(root))
	reactor.run()

