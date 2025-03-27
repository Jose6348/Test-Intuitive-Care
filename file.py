import requests
from bs4 import BeautifulSoup
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
if response.status_code != 200:
    print("Erro ao acessar o site:", response.status_code)
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

anexo_i_link = None
anexo_ii_link = None

links = soup.find_all('a')
for link in links:
    href = link.get('href', '')
    text = link.get_text(strip=True).lower()
    
    if "anexo i" in text and "anexo ii" not in text and href.endswith('.pdf'):
        anexo_i_link = link
    elif "anexo ii" in text and href.endswith('.pdf'):
        anexo_ii_link = link

if not anexo_i_link or not anexo_ii_link:
    print("Anexos não encontrados. Aqui estão todos os links encontrados na página:")
    for link in links:
        href = link.get('href', '')
        text = link.get_text(strip=True)
        if href:  # Exibe apenas links com href
            print(f"Texto: {text}, URL: {href}")
    exit()

anexo_i_url = anexo_i_link['href']
anexo_ii_url = anexo_ii_link['href']

base_url = "https://www.gov.br"
anexo_i_url = anexo_i_url if anexo_i_url.startswith('http') else base_url + anexo_i_url
anexo_ii_url = anexo_ii_url if anexo_ii_url.startswith('http') else base_url + anexo_ii_url

print("Anexo I URL:", anexo_i_url)
print("Anexo II URL:", anexo_ii_url)

anexo_i_response = requests.get(anexo_i_url)
anexo_ii_response = requests.get(anexo_ii_url)

with open('anexo_I.pdf', 'wb') as f:
    f.write(anexo_i_response.content)

with open('anexo_II.pdf', 'wb') as f:
    f.write(anexo_ii_response.content)

with zipfile.ZipFile('anexos.zip', 'w') as zipf:
    zipf.write('anexo_I.pdf')
    zipf.write('anexo_II.pdf')

print("Anexos baixados e compactados em 'anexos.zip' com sucesso!")
