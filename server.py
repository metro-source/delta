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
from http.server import HTTPServer
from request_handler import RequestHandler

def run_server(server=HTTPServer, handler=RequestHandler):
    addr = ('0.0.0.0', 12221)
    proxyd = server(addr, handler)

    print("Metro Delta Started")
    proxyd.serve_forever()

if __name__ == '__main__':
    run_server()