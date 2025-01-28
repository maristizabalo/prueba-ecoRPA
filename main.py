from src.downloader import Downloader
from src.data_processor import DataProcessor
from src.email_sender import EmailSender


# Configuración inicial
BASE_URL = "https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/precios-de-venta-al-publico-de-articulos-de-primera-necesidad-pvpapn"
TITLE = "Precios de los productos de primera necesidad para los colombianos en tiempos del COVID-19"
DOWNLOAD_KEYWORD = "Anexo referencias mas vendidas"
DOWNLOAD_DIR = "downloads"
OUTPUT_DIR = "output"

# Configuración del correo
EMAIL_SENDER = "pruebamaicolecorpa@gmail.com"
PASSWORD = "qtis svuw yzsz vycv"
EMAIL_RECEIVER = "maristizabalo95@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
PORT = 587


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
    
    print("2. Procesar los datos y generarel Archivo")
    
    # instancia del procesador de datos
    processor = DataProcessor(file_path, OUTPUT_DIR)
    
    processor.load_data()
    processor.extract_relevant_data()
    top_10 = processor.get_top_10_products()
    processor.generate_new_file(top_10)
    summary = processor.calculate_summary()
    
    print("3. Enviar correo")
    
    # variables con la data solicitada en el correo pero tambien anexado
    total_products = summary["Total productos vendidos"]
    top_10_total = summary["Total 10 productos más vendidos"]
    percentage = summary["Porcentaje del total"]

    body = (
        f"Hola,\n\n"
        f"Esta es mi prueba para el cargo de Desarrollador de Automatizacion en Python.\n\n"
        f"A continuacion pueden ver el resumen solicitado:\n\n"
        f"- Total de productos vendidos: {total_products}\n"
        f"- Total de los 10 productos más vendidos: {top_10_total}\n"
        f"- Porcentaje de los 10 productos más vendidos: {percentage:.2f}%\n\n"
        f"Adjunto tambien los archivos de los 10 productos y un archivo con el resumen de las estaditicas solicitadas.\n\n"
        f"Información de contacto:\n"
        f"- Correo electrónico: maristizabalo95@gmail.com\n"
        f"- Teléfono: +57 3113652025\n\n"
        f"Quedo atento a cualquier requerimiento adicional.\n\n"
        f"Saludos cordiales,\n"
        f"Maicol Jacobo Aristizabal Obando"
    )

    # archivos a adjuntar
    attachments = [
        f"{OUTPUT_DIR}/top_10_productos.csv",
        f"{OUTPUT_DIR}/resumen.csv"
    ]

    # envio del correo
    email_sender = EmailSender(SMTP_SERVER, PORT, EMAIL_SENDER, PASSWORD)
    email_sender.send_email(
        recipient_email=EMAIL_RECEIVER,
        subject="Resumen de Ventas - Top 10 Productos",
        body=body,
        attachment_paths=attachments
    )
    
if __name__ == "__main__":
    main()


