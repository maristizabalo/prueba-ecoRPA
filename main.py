import requests
from bs4 import BeautifulSoup
import os

# variables iniciales para url y folder de descargas
BASE_URL = "https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/precios-de-venta-al-publico-de-articulos-de-primera-necesidad-pvpapn"
DOWNLOAD_DIR = "downloads"

# creamos la carpeta de descargas si no existe
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

#funcion encargada de descargar el contenido de la pagina
def fetch_page(url):
    print("descargando pagina")
    response = requests.get(url)
    response.raise_for_status()
    print("todo en orden")
    return response.text

def main():
    print("inicio de proyecto")
    print(f"URL base: {BASE_URL}")
    
    # Descargar la página
    html_content = fetch_page(BASE_URL)
    print("HTML descargado", html_content)

if __name__ == "__main__":
    main()