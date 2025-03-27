import os
import re
import requests
import zipfile

base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
anos = [2023, 2024]

os.makedirs("demonstracoes", exist_ok=True)

for ano in anos:
    url_pasta = f"{base_url}{ano}/"
    resp = requests.get(url_pasta)
    if resp.status_code == 200:
        pasta_ano = os.path.join("demonstracoes", str(ano))
        os.makedirs(pasta_ano, exist_ok=True)
        arquivos = re.findall(r'href="([^"]+\.zip)"', resp.text)
        for arquivo in arquivos:
            arquivo_url = url_pasta + arquivo
            caminho_local = os.path.join(pasta_ano, arquivo)
            print(f"Baixando {arquivo_url} ...")
            resp_arq = requests.get(arquivo_url)
            if resp_arq.status_code == 200:
                with open(caminho_local, "wb") as f:
                    f.write(resp_arq.content)
                print(f"Salvo: {caminho_local}")
                try:
                    with zipfile.ZipFile(caminho_local, "r") as z:
                        z.extractall(pasta_ano)
                        print(f"Arquivo {arquivo} extraído na pasta {pasta_ano}")
                except zipfile.BadZipFile:
                    print(f"Aviso: {arquivo} não pôde ser extraído (arquivo ZIP inválido)")
            else:
                print(f"Erro ao baixar {arquivo_url} (status {resp_arq.status_code})")
    else:
        print(f"Erro ao acessar {url_pasta} (status {resp.status_code})")

cadop_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
print(f"Baixando {cadop_url} ...")
resp_cadop = requests.get(cadop_url)
if resp_cadop.status_code == 200:
    with open("relatorio_cadop.csv", "wb") as f:
        f.write(resp_cadop.content)
    print("Salvo: relatorio_cadop.csv")
else:
    print(f"Erro ao baixar {cadop_url} (status {resp_cadop.status_code})")
