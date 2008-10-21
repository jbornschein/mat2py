function mat2py_init()
% Initialie mat2py layer.
% This functions sets some globale variables starting with the mat2py_
% prefix which are used by other mat2py_* functions.

global mat2py_url
global mat2py_xcp

mat2py_url='http://localhost:8080/mat2py/';
mat2py_xcp='/tmp/mat2py_xcp.mat';

end
