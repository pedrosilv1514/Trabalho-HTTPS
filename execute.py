from threading import Thread
from servidor import start_server
from cliente import http_client

server_thread = Thread(target=start_server, daemon=True)

server_thread.start()

http_client()