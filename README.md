# Script utiles de python

Este es un proyecto que realizo como hobby, en el cual trato de aplicar buenas prácticas de desarrollo de software. Por medio de una interfaz gráfica, centralizo y gestiono diferentes scripts de Python que realizan tareas diversas, ya sea para facilitar mi día a día o para realizar actividades que me gusta hacer.

---

## **Estructura del Proyecto**

```
central_project/
├── main.py                   # Punto de entrada principal
├── ui/
│   ├── app_ui.py             # Interfaz gráfica del centralizador
├── services/
│   ├── project_service.py    # Lógica para manejar los proyectos
├── projects/
│   ├── pomodoro/
│   │   ├── main.py           # Main del proyecto Pomodoro
│   │   ├── services/
│   │   ├── ui/
│   ├── daily_update/
│   │   ├── main.py           # Main del proyecto Daily Update
│   │   ├── services/
│   │   │   ├── news_service.py
│   │   │   ├── horoscope_service.py
│   │   │   ├── history_service.py
│   │   ├── ui/
│   │   │   ├── app_ui.py
│   │   ├── config/
│   │   │   ├── config.json
├── tests/
│   ├── test_project_service.py
│   ├── test_timer_service.py
│   ├── test_horoscope_service.py
│   ├── test_news_service.py
│   ├── test_history_service.py
├── README.md                 # Documentación del proyecto
└── requirements.txt          # Dependencias comunes
```

---

## **Requisitos Previos**

Antes de ejecutar el proyecto, asegúrate de tener instalado:

1. **Python 3.8 o superior**
2. **pip** (Administrador de paquetes de Python)
3. Opcional: un entorno virtual para gestionar las dependencias del proyecto.

---

## **Instalación**

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/central_project.git
   cd central_project
   ```

2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Uso del Centralizador**

1. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

2. Aparecerá una interfaz gráfica donde podrás:
   - Ver la lista de proyectos disponibles.
   - Ejecutar cualquier proyecto seleccionado.
   - Refrescar la lista de proyectos.
   - Salir del centralizador.

---

## **Proyectos Disponibles**

### **1. Pomodoro**
Un temporizador que sigue la técnica Pomodoro para mejorar la productividad, con opciones para iniciar, pausar y reiniciar.

### **2. Daily Update**
Este proyecto muestra información diaria en una interfaz gráfica, incluyendo:
- Noticias del día.
- Horóscopo diario para un signo seleccionado.
- Eventos históricos ocurridos en la fecha actual.

---


## **Ejecución de Tests**

1. Para ejecutar todos los tests del proyecto:
   ```bash
   pytest
   ```

2. Para ejecutar los tests de un módulo específico, por ejemplo, `project_service`:
   ```bash
   pytest tests/test_project_service.py
   ```

3. Generar un reporte detallado:
   ```bash
   pytest -v
   ```

---

## **Estructura de Subproyectos**

Cada subproyecto tiene la siguiente estructura básica:

```
projects/
├── nombre_proyecto/
│   ├── main.py          # Punto de entrada del proyecto
│   ├── services/        # Lógica específica del proyecto
│   ├── ui/              # Interfaz gráfica del proyecto (opcional)
```

Puedes agregar nuevos subproyectos simplemente creando una nueva carpeta en `projects/` con su propio archivo `main.py`.

---

## **Contribuciones**

Si deseas contribuir a este proyecto:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad o corrección:
   ```bash
   git checkout -b nueva_funcionalidad
   ```
3. Haz tus cambios y realiza commits:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía un pull request.

---

## **Licencia**

Este proyecto está licenciado bajo la [MIT License](https://opensource.org/licenses/MIT).

