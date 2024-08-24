import subprocess

# Caminho para o arquivo desafio-python.py
caminho_desafio = "desafio-python.py"

# Caminho para o arquivo testes.txt
caminho_testes = "testes.txt"

# Conjunto para armazenar as características já processadas
caracteristicas_processadas = set()

# Ler as características de teste do arquivo testes.txt
with open(caminho_testes, "r") as arquivo:
    for linha in arquivo:
        caracteristica_fornecida = linha.strip()
        if caracteristica_fornecida not in caracteristicas_processadas:
            # Executar o código principal com a característica fornecida como entrada
            resultado = subprocess.run(
                ["python3", caminho_desafio, caracteristica_fornecida],
                capture_output=True,
                text=True
            )
            # Imprimir o resultado do teste
            print(f"Característica: {caracteristica_fornecida}, Resultado: {resultado.stdout.strip()}")
            caracteristicas_processadas.add(caracteristica_fornecida)