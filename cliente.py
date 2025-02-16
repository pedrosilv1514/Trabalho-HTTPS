import requests
import logging

logging.basicConfig(filename="client.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def http_client():
    try:
        response = requests.get('https://localhost:4443', verify=False)
        logging.info(f"Resposta recebida: {response.text}")
        print("Resposta do servidor: ", response.text)
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na conexão HTTPS: {e}")
if __name__ == "__main__":
    http_client()