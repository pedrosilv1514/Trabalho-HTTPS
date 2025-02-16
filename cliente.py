import requests

def http_client():
    try:
        response = requests.get('https://localhost:4443', verify=False)
        print("Resposta do servidor: ", response.text)
    except requests.exceptions.RequestException as e:
        print("Erro na conexão HTTPS: ", e)

if __name__ == "__main__":
    http_client()