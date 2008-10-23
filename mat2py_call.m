function varargout = mat2py_call(func_name, varargin)
% 

global mat2py_url;
global mat2py_xpath;

save(mat2py_xpath, 'varargin')

msg = createSoapMessage('urn:lal', 'call', {func_name}, {'name'} );
res = parseSoapResponse( callSoapService(mat2py_url, 'call', msg) );

ret = load(mat2py_xpath);
for i = 1:10
    fname = strcat( 'ret', int2str(i) );
    if isfield(ret, fname)
        varargout{i} = ret.(fname);
    end
end
        
end
