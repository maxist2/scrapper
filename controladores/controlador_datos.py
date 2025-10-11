import json
import os


class Archivador:
    """
    Archivador genérico que maneja almacenamiento temporal y final de datos en JSON.
    Permite agregar elementos con IDs automáticos y moverlos a un archivo final bajo una categoría.
    """

    def __init__(self, temporal="temporal.json", final="datos.json"):
        self.archivo_temp = temporal
        self.archivo_final = final

        # Crear archivo temporal si no existe
        if not os.path.exists(self.archivo_temp):
            with open(self.archivo_temp, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    # --------------------------------------------------

    def _leer_json(self, ruta):
        """Lee un archivo JSON y devuelve su contenido o el tipo vacío adecuado."""
        try:
            with open(ruta, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return [] if ruta == self.archivo_temp else {}

    # --------------------------------------------------

    def agregar(self, elementos):
        """
        Agrega elementos (lista o único) al archivo temporal con IDs consecutivos.
        Acepta dicts o instancias con atributos (.__dict__).
        """
        if not isinstance(elementos, list):
            elementos = [elementos]

        data = self._leer_json(self.archivo_temp)

        # Calcular último ID
        ids = []
        for e in data:
            try:
                ids.append(int(list(e.keys())[0]))
            except Exception:
                continue
        ultimo_id = max(ids) if ids else 0

        nuevos = []
        id_actual = ultimo_id + 1

        for e in elementos:
            if isinstance(e, dict):
                nuevos.append({str(id_actual): e})
            elif hasattr(e, "__dict__"):
                nuevos.append({str(id_actual): e.__dict__})
            else:
                print(f"Objeto no serializable ignorado: {e}")
                continue
            id_actual += 1

        data.extend(nuevos)

        with open(self.archivo_temp, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"{len(nuevos)} elemento(s) agregado(s) temporalmente.")
        return data

    # --------------------------------------------------

    def finalizar(self, categoria="default"):
        """
        Mueve los datos del temporal al archivo final agrupándolos bajo una categoría.
        Luego limpia el archivo temporal.
        """
        temporales = self._leer_json(self.archivo_temp)
        if not temporales:
            print("No hay datos temporales para guardar.")
            return

        final = self._leer_json(self.archivo_final)
        if isinstance(final, list):
            final = {"default": final}

        final[categoria] = temporales

        with open(self.archivo_final, "w", encoding="utf-8") as file:
            json.dump(final, file, ensure_ascii=False, indent=4)

        with open(self.archivo_temp, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)

        print(
            f"Guardados {len(temporales)} elemento(s) en '{self.archivo_final}' bajo '{categoria}'."
        )

    # --------------------------------------------------

    def listar_temporales(self):
        """Muestra los datos temporales actuales."""
        data = self._leer_json(self.archivo_temp)
        print(json.dumps(data, ensure_ascii=False, indent=4))
        return data

    # --------------------------------------------------

    def limpiar_temporal(self):
        """Borra el contenido del archivo temporal."""
        with open(self.archivo_temp, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        print("Archivo temporal limpiado.")
