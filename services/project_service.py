import subprocess
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


class ProjectService:
    def __init__(self, projects_path):
        self.projects_path = projects_path

    def execute_project(self, project_name):
        project_path = os.path.join(self.projects_path, project_name, "main.py")
        if os.path.exists(project_path):
            subprocess.run(["python", project_path])
        else:
            print(f"El proyecto {project_name} no tiene un archivo main.py válido.")

    def list_projects(self):
        return [dir for dir in os.listdir(self.projects_path) if os.path.isdir(os.path.join(self.projects_path, dir))]
