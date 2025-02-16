import http.server
import ssl
import logging

# Inicialização de um servidor localizado no local-host porta 4433

logging.basicConfig(filename="server.log",level=logging.INFO, format="(asctime)s - %(message)s")

class secureHTTPServer(http.server.HTTPServer):
    def __init__(self, server_address, handler_class, certfile, keyfile):
        super().__init__(server_address, handler_class)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        self.socket = context.wrap_socket(self.socket, server_side=True)
        
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Requisição recebida de: {self.client_address}")
        self.send_response(200)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        self.wfile.write(b"Conexao Segura!")
        logging.info("Resposta enviada com sucesso.")

def start_server():
    server_address = ("localhost", 4443)
    httpd = secureHTTPServer(server_address, RequestHandler, 'certs/cert.pem', 'certs/key.pem')
    print("Servidor HTTPS Rodando em https://localhost:4443")
    httpd.serve_forever()

if __name__ == '__main__':
    start_server()