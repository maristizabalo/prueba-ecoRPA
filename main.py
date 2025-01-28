from src.downloader import Downloader
from src.data_processor import DataProcessor

# Configuración inicial
BASE_URL = "https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/precios-de-venta-al-publico-de-articulos-de-primera-necesidad-pvpapn"
TITLE = "Precios de los productos de primera necesidad para los colombianos en tiempos del COVID-19"
DOWNLOAD_KEYWORD = "Anexo referencias mas vendidas"
DOWNLOAD_DIR = "downloads"
OUTPUT_DIR = "output"

def main():
    print("1. Acceder al Sitio Web")
    
    # instancia del descargador
    downloader = Downloader(BASE_URL, DOWNLOAD_DIR)
    html_content = downloader.fetch_page()
    # print(f"pagina obtenida -------------------------- {html_content} --------------------------")

    # obtener href del archivo
    file_url = downloader.find_table_and_link(html_content, TITLE, DOWNLOAD_KEYWORD)

    # descargar el archivo en la carpeta de descargas
    file_path = downloader.download_file(file_url)
    print(f"descarga completa en la ruta: {file_path}")
    
    print("2. Procesar el Archivo")
    
    # instancia del procesador de datos
    processor = DataProcessor(file_path, OUTPUT_DIR)
    
    processor.load_data()
    processor.extract_relevant_data()
    top_10 = processor.get_top_10_products()
    processor.generate_new_file(top_10)
    
if __name__ == "__main__":
    main()