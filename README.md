# Proyecto EcoRPA

Este proyecto utiliza **Python 3.11.9** específicamente.

## Clonar el proyecto

Primero, clona el proyecto desde el repositorio:

```
git clone https://github.com/maristizabalo/prueba-ecoRPA.git
```

Luego, navega a la carpeta del proyecto:

```
cd prueba-ecoRPA
```

## Crear y activar un entorno virtual

Crea un entorno virtual:

```
python -m venv venv
```

Activa el entorno virtual:

- En **Windows**:

    ```
    .\venv\Scripts\activate
    ```

- En **Linux**:

    ```
    source venv/bin/activate
    ```

## Instalar dependencias

Con el entorno virtual activo, instala las librerías necesarias:

```
pip install -r requirements.txt
```

## Configuración y ejecución

Desde el archivo `main.py`, puedes modificar las variables según sea requerido. Luego, ejecuta el script:

```
python main.py
```

Esto creará dos carpetas: `downloads` y `output`.

- En `downloads` estarán los archivos descargados de la página del DANE.
- En `output` tendrás los archivos de salida, como el top 10 de productos más vendidos y el resumen de totales del archivo original solicitados.

Además, el script enviará un correo electrónico con los archivos adjuntos y un cuerpo de correo ya definido.