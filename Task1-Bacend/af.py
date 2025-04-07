from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/numbers/"):
            number_type = self.path.split("/")[-1]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "windowPrevState": [],
                "windowCurrState": [1, 3, 5, 7],
                "numbers": [1, 3, 5, 7],
                "avg": 4.0
            }
            self.wfile.write(str(response).replace("'", '"').encode())

PORT = 9876
server = HTTPServer(('localhost', PORT), MyHandler)
print(f"Server running at http://localhost:{PORT}")
server.serve_forever()