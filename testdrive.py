#!/usr/bin/python

import sys
import time
import mat2py

"""
 This Script exports two functions to Matlab.

 The first one, "ping" blocks for 3 seconds and returns a 0
 The second one prints the given arguments an returns some values
"""



def ping():
	print "ping() called"
	time.sleep(3)
	return 0

def hello(a, b):
	print "Hello!"
	print "  a=", a
	print "  b=", b
	return a,b,a*b

mat2py.reg_func(ping,  "ping")
mat2py.reg_func(hello, "hello")
mat2py.run()

