import pandas as pd
import os

class DataProcessor:
    def __init__(self, file_path, output_dir):
        self.file_path = file_path
        self.df_original = None
        self.df_clean = None
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def load_data(self):
        
        try:
            # cargar la hoja 1 del archivo Excel que tiene las cantidades totales por producto
            self.df_original = pd.read_excel(self.file_path, sheet_name=1, skiprows=7)
            self.df_original = self.df_original.iloc[:-1]
             # Convertir las columnas de 'Cantidad' y 'Precio' a números enteros
            self.df_original["Cantidades vendidas "] = self.df_original["Cantidades vendidas "].astype(int)
            self.df_original["Precio Reportado "] = self.df_original["Precio Reportado "].astype(int)
            self.df_original = self.df_original.sort_values(by='Cantidades vendidas ', ascending=False)
            print("datos cargados exitosamente")
        except Exception as e:
            raise ValueError(f"Error al cargar los datos: {e}")
        
    def extract_relevant_data(self):
        print(self.df_original)
        # columnas relevantes
        relevant_columns = ["Nombre producto", "Marca", "Precio Reportado ", "Cantidades vendidas "]

        # validar que existan las columnas en el dataframe
        if not set(relevant_columns).issubset(self.df_original.columns):
            raise ValueError(f"El archivo no contiene todas las columnas necesarias: {relevant_columns}")

        # extraemos unicamente lascolumnas solicitaas
        self.df_clean = self.df_original[relevant_columns]
        print("Extracción completada.")

    def get_top_10_products(self):
        print("obteniendo el top de 10 productos mas vendidos")
        top_10 = self.df_clean.nlargest(10, "Cantidades vendidas ").copy()
        print("top 10 obtenido", top_10)
        return top_10

    def generate_new_file(self, top_10):
        print("...se está generando el archivo con el top 10 de productos más vendidos...")
    
        # eliminar columna especifca la columna "Cantidades vendidas"
        if "Cantidades vendidas " in top_10.columns:
            top_10 = top_10.drop(columns=["Cantidades vendidas "])
            print("Se eliminó la columna 'Cantidades vendidas'.")
    
        # renombrar las columnas segun solicitado en la prueba
        new_column_names = {
            "Nombre producto": "Nombre del Producto",
            "Precio Reportado ": "Precio"
        }
        top_10.rename(columns=new_column_names, inplace=True)
        print("Nombres de columnas actualizados:", top_10.columns.tolist())
    
        # calcular total de precios
        total_price = top_10["Precio"].sum()
    
        # crear una fila vacia y otra con el total de precios
        empty_row = pd.DataFrame([["", "", ""]], columns=top_10.columns)
        summary_row = pd.DataFrame([{
            "Nombre del Producto": "",
            "Marca": "TOTAL SUMA DE PRECIOS",
            "Precio": total_price
        }])
    
        # concatenar las filas al final del dataframe
        result = pd.concat([top_10, empty_row, summary_row], ignore_index=True)
    
        # archivo de salida
        output_path = os.path.join(self.output_dir, "top_10_productos.csv")
    
        # guardar archvo en formato CSV con separador de ;
        result.to_csv(output_path, sep=";", index=False, header=True)
    
        print(f"Archivo generado exitosamente en: {output_path}")

    