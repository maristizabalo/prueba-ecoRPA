import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

class EmailSender:
    def __init__(self, smtp_server, port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body, attachment_paths):
        
        #try catch para intentar enviar el mensaje y manejar el error en caso de fallo
        try:
            
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = subject

            # cuerpo del mensae
            message.attach(MIMEText(body, "plain"))

            # adjunto de archivos
            for attachment_path in attachment_paths:
                if attachment_path and os.path.exists(attachment_path):
                    with open(attachment_path, "rb") as attachment:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={os.path.basename(attachment_path)}",
                    )
                    message.attach(part)

            # conectar al servidor smtp y enviar el mensaje
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
            print("Envio exitoso")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")