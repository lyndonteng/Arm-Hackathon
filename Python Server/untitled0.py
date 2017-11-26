# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:22:53 2017

@author: Lyndon Teng
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
#import logging
import socket
from Hackathon_megaHax import openLocation, getDictList, writeDictList
#from dotp import xyznumpyFromDict, dotp, lasernumpyFromDict
from random import randint
#from untitled2 import ddisplacement,vv,abs_vel

height=[1,2,3,4,5,6]

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        content = b"GET: Hello World!"# store as bytes instead of string
        self._set_response()
        self.send_header('Content-Length', len(content))
        self.wfile.write(content)
        
        cont_length=self.headers['Content-Length']
        print(cont_length)
        if cont_length is not None:
            post_data = self.rfile.read(int(cont_length))
            print(post_data)
        else:
            return None

    def do_PUT(self):
        content = b"PUT: Hello, Mbed!"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)
        cont_length=self.headers['Content-Length']
        #print(cont_length)
        if cont_length is not None:
            post_data = self.rfile.read(int(cont_length))
            print(post_data)
            mystring=post_data.decode("utf-8")
            print(mystring)
        else:
            return None
        
        #first we need to get a dictlist from the data
        dictList = getDictList(mystring)

        #now we generate displacement from the list
        displacementDictList = dictList # here we append extra data addDisplacement(dictList)
        #changeinheight= ddisplacement(height)
        #vertv=vv(displacementDictList)
        #absv=abs_vel(displacementDictList)
        #print(changeinheight,vertv,absv)
        
        
        #write data to csv
        writeDictList(displacementDictList,"item{}".format(randint(0,10000)),r"D:\OneDrive\Documents\Part 1A\Hackathon Data")
        
    
    
def run(server_class=HTTPServer, handler_class=S, port=5000):
    server_address = ('', port)
    print("HTTP server running on port "+str(port))
    print("Your IP address is: ", socket.gethostbyname(socket.gethostname()))
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()