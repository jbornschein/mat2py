#!/usr/bin/python

"""
  mat2py -- some documentation
"""

from scipy import io as matio
from twisted.internet import reactor
from twisted.web import soap,resource,server

# Registered functions dictionary
funcs = {}

# Actual Webservice object
class M2PSOAP(soap.SOAPPublisher):
	"""	Webservice object used internally by mat2py
	"""
	def __init__(self, xpath):
		soap.SOAPPublisher()
		self.xpath = xpath
		
	def soap_getxpath(self):
		return self.xpath

	def soap_call(self, name):
		mat = matio.loadmat(self.xpath)
		args = list( mat['varargin'] )
		try:
			func = funcs[name]
			ret = func(*args)
		except:
			print "Could not call %s with args %s" % (name, args)
		d = {}
		if isinstance(ret, tuple):
			for i in range(len(ret)):
				d["ret%d"%(i+1)] = ret[i] 
		else:
			d["ret1"] = ret
		matio.savemat(self.xpath, d)

def reg_func(func, name):
	""" Register the given funtion under the specified name to matlab"""
	funcs[name] = func

def run(port=8080, path="/tmp/mat2py_xcp.mat"):
	""" Run event-loop and wait for incoming requests on the specified port. Use the 
		given file path xfor data exchange.

		This funtion does not return.
	"""
	print "Starting Webservice on http://localhost:%d. Data exchange file is '%s'" % (port,path)
	m2p = M2PSOAP(path)
	root = resource.Resource()
	root.putChild('mat2py', m2p)
	reactor.listenTCP(port, server.Site(root))
	reactor.run()

