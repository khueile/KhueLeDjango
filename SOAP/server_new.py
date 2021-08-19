
# http://spyne.io/docs/2.10/

#  Application is the glue between one or more service definitions, interface and protocol choices
from spyne.application import Application#webserver apacheIIS..WSGI asgi
# The @srpc decorator exposes methods as remote procedure calls and declares the data types it accepts and returns.
from spyne.decorator import srpc
# spyne.service.ServiceBase is the base class for all service definitions.
from spyne.service import ServiceBase

from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String

# Our server is going to use HTTP as transport,
# so we import the WsgiApplication from the :mod:`spyne.server.wsgi module.
# It’s going to wrap the Application instance.
from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11


# We start by defining our service. The class name will be made public in the wsdl document
class FibService(ServiceBase):
    
    @srpc(UnsignedInteger, _returns=String)#wsdl
    def fib(n):
        a = 0
        b = 1
        final = ''


        while True:
            currnumber=a+b
            if currnumber<n:
                final = final + str(currnumber)+ ' '
            else:
                break
            a=b
            b=currnumber


        return final






if __name__=='__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    app = Application([FibService], # SOAP WEB SERVICE
                      tns='spyne.examples.hello',
                      in_protocol=Soap11(), #
                      out_protocol=Soap11(), #
         #'spyne.examples.hello.http',
         #in_protocol=Soap11(validator='lxml'),
         #out_protocol=Soap11(),
    )
    wsgi_app = WsgiApplication(app) # WSGI
    server = make_server('0.0.0.0', 3333, wsgi_app)

    print("listening to http://127.0.0.1:3333")
    print("wsdl is at: http://localhost:3333/?wsdl")

    server.serve_forever()