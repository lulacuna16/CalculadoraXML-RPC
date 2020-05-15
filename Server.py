from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('192.168.1.64', 56432),requestHandler=RequestHandler) as Server:
    Server.register_introspection_functions()

    def suma(x, y):
        return x + y
    Server.register_function(suma)
    def resta(x, y):
        return x - y
    Server.register_function(resta)
    def multi(x, y):
        return x * y
    Server.register_function(multi)
    def div(x, y):
        return x/y
    Server.register_function(div)

    print("Servidor iniciado")
    Server.serve_forever()