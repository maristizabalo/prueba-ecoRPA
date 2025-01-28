import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

class Downloader:
    def __init__(self, base_url, download_dir="downloads"):
        self.base_url = base_url
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)

    def fetch_page(self):
        # print("iniciando funcion para obtener pagina")
        response = requests.get(self.base_url)
        response.raise_for_status()
        # print("fetch correto")
        return response.text

    def find_table_and_link(self, html, title_keyword, download_keyword):
        # print("iniciando funcion para encontrar tabla y enlace")
        # print(f"titulo a buscar: {title_keyword}")
        soup = BeautifulSoup(html, "html.parser")
        
        # encontrando etiqueta con el titulo solicitado
        h2_tag = soup.find("h2", class_="subtitle-min", string=lambda text: title_keyword in text if text else False)
        # print(f"titulo encontrado: {h2_tag}")
        if not h2_tag:
            raise ValueError(f"no se encontro ningun titulo")
        
        # busca la tabla padre que contiene la etiqueta h2 buscada
        parent_table = h2_tag.find_parent("table")
        if not parent_table:
            raise ValueError("no e encontro ninguna tabla padre")
        
        # busca el enlace con el atributo title solicitado
        link = parent_table.find("a", title=download_keyword)
        if not link:
            raise ValueError(f"no se encontró ningún enlace con el título solicitado")
        
        # obtener el href local y convertirlo en un enlace completo
        href = link['href']
        full_url = urljoin(self.base_url, href)
        return full_url

    def download_file(self, file_url):
        
        # cambiando nombre del archivo a descarga
        file_name = "precios.xlsx"
        file_path = os.path.join(self.download_dir, file_name)
        
        # print(file_url)
        response = requests.get(file_url)
        response.raise_for_status()
        
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("descargado correctamente")
        return file_path