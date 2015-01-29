#!/usr/bin/env python

# CMPUT 410 Lab3
# Dylan Stankievech
# Jan 28, 2015
#
# This code copied from in-class presentation

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/cgi"]
httpd = server(server_address, handler)
print "Starting server..."
httpd.serve_forever()