from tkinter import Tk
from services.project_service import ProjectService
from ui.app_ui import CentralAppUI

if __name__ == "__main__":
    # Ruta donde se encuentran los proyectos
    projects_path = "projects"
    project_service = ProjectService(projects_path)

    root = Tk()
    app = CentralAppUI(root, project_service)
    root.mainloop()
