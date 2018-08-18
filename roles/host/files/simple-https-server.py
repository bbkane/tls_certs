#!/usr/bin/env  python

# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443

import BaseHTTPServer, SimpleHTTPServer
import ssl

ip = '0.0.0.0'
port = 4443

print "ip:", ip
print "port:", port

httpd = BaseHTTPServer.HTTPServer((ip, port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./host.pem', server_side=True)
httpd.serve_forever()
