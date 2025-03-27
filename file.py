import requests
from bs4 import BeautifulSoup
import zipfile

# Passo 1: Acessar o site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
if response.status_code != 200:
    print("Erro ao acessar o site:", response.status_code)
    exit()

# Passo 2: Parsear o HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Passo 3: Encontrar os anexos
anexo_i_link = None
anexo_ii_link = None

# Busca todos os links <a> na página
links = soup.find_all('a')
for link in links:
    href = link.get('href', '')
    text = link.get_text(strip=True).lower()
    # Verifica se o texto contém "anexo i" e se o link termina em .pdf
    if "anexo i" in text and href.endswith('.pdf'):
        anexo_i_link = link
    # Verifica se o texto contém "anexo ii" e se o link termina em .pdf
    if "anexo ii" in text and href.endswith('.pdf'):
        anexo_ii_link = link

# Verificação
if not anexo_i_link or not anexo_ii_link:
    print("Anexos não encontrados. Aqui estão todos os links encontrados na página:")
    for link in links:
        href = link.get('href', '')
        text = link.get_text(strip=True)
        if href:  # Exibe apenas links com href
            print(f"Texto: {text}, URL: {href}")
    exit()

# Passo 4: Extrair URLs
anexo_i_url = anexo_i_link['href']
anexo_ii_url = anexo_ii_link['href']

# Se os URLs forem relativos, adicionar a base
base_url = "https://www.gov.br"
anexo_i_url = anexo_i_url if anexo_i_url.startswith('http') else base_url + anexo_i_url
anexo_ii_url = anexo_ii_url if anexo_ii_url.startswith('http') else base_url + anexo_ii_url

# Passo 5: Baixar os PDFs
anexo_i_response = requests.get(anexo_i_url)
anexo_ii_response = requests.get(anexo_ii_url)

with open('anexo_I.pdf', 'wb') as f:
    f.write(anexo_i_response.content)
with open('anexo_II.pdf', 'wb') as f:
    f.write(anexo_ii_response.content)

# Passo 6: Compactar em ZIP
with zipfile.ZipFile('anexos.zip', 'w') as zipf:
    zipf.write('anexo_I.pdf')
    zipf.write('anexo_II.pdf')

print("Anexos baixados e compactados em 'anexos.zip' com sucesso!")