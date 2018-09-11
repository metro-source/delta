"""

    Metro Delta - HTTP Proxy cache using delta encoding
    Copyright (C) 2018 Metro

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    For more information, contact the following email:
    contact@metrodev.io
"""
from http.server import BaseHTTPRequestHandler
from http.client import HTTPConnection

class RequestHandler(BaseHTTPRequestHandler):
    """
        Should define
        do_GET <- all others should just pass it on 
        do_HEAD
        do_POST
        do_PATCH
        do_PUT
        do_DELETE        
    """
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

        self.host = self.headers['Host']
        self.content_type = self.headers['Content-Type']
        self.server_version = "Metro Delta/1.0.0 (%s)" % self.sys_version

    """
        Forward the incoming request to the appropiate target
    """
    def forward_request(self):
        self.log_message("Forwarding request (%s) to %s", self.headers['Host'], self.path)

        connection = HTTPConnection(self.headers['Host'])
        connection.request(self.command, self.path)
        
        response = connection.getresponse()

        print("Got response")

        return response.read()

    def do_GET(self):
        self.log_request()

        data = self.forward_request()

        print("Data %s" % data)

        self.send_response(200, "Got it")

        self.wfile.write(data)
