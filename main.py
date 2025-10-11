from spider.extractor import obtener_datos
from controladores.controlador_datos import mostrar_datos

if __name__ == "__main__":
    datos = obtener_datos("https://example.com")
    mostrar_datos(datos)
