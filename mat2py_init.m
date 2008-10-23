function mat2py_init(port)
% Initialie mat2py layer.
% This functions sets some globale variables starting with the mat2py_
% prefix which are used by other mat2py_* functions.

global mat2py_url
global mat2py_xpath

mat2py_url = strcat('http://localhost:', int2str(port));
mat2py_url = strcat(mat2py_url, '/mat2py/');

msg = createSoapMessage('urn:lal', 'getxpath', {}, {} );
res = parseSoapResponse( callSoapService(mat2py_url, 'getxpath', msg) );

mat2py_xpath=res;


end
