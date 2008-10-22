#!/usr/bin/python

import sys
import mat2py

"""
 This Script exports two functions to Matlab.

 The first one, "ping" blocks for 3 seconds and returns a 0
 The second one prints the given arguments an returns some values
"""



def ping():
	time.sleep(3)
	print "ping() called"

def hello(a, b):
	print "Hello!"
	print "  a=", a
	print "  b=", b
	return a,b,a*b

mat2py.reg_func("ping", ping)
mat2py.reg_func("hello", hello)
mat2py.run()

