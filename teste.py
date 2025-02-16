import subprocess

def testar_comunicao():
    print("Teste de comunicação com o servidor...")
    resultado = subprocess.run(["curl", "-k", "https://localhost:4443"], capture_output=True, text=True)
    if "Conexao segura" in resultado.stdout:
        print("Teste bem-sucedido! Comunicação segura funcionando")
    else:
        print("Erro na comunicação")

testar_comunicao()