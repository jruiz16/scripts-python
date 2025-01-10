import json
import os


class ConfigManager:
    def __init__(self, config_path=None):
        """
        Inicializa el ConfigManager cargando el archivo de configuración especificado.
        :param config_path: Ruta del archivo de configuración JSON.
        """
        if config_path is None:
            raise ValueError("Se debe proporcionar la ruta del archivo de configuración.")
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        """Carga el archivo JSON de configuración."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"No se encontró el archivo de configuración: {self.config_path}")
        with open(self.config_path, "r") as f:
            return json.load(f)

    def get(self, *keys, default=None):
        """
        Obtiene un valor anidado desde la configuración.
        :param keys: Claves en orden jerárquico.
        :param default: Valor por defecto si no se encuentra la clave.
        :return: Valor correspondiente a las claves especificadas o el valor por defecto.
        """
        value = self.config
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key, default)
            else:
                return default
        return value
