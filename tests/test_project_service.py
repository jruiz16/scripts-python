import pytest  # noqa: F401
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from services.project_service import ProjectService

def test_list_projects():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../projects"))
    project_service = ProjectService(projects_path=base_path)
    projects = project_service.list_projects()
    assert len(projects) > 0  # Asumiendo que hay proyectos en la carpeta

def test_execute_project():
    project_service = ProjectService(projects_path="projects")
    project_service.execute_project("pomodoro")  # Ejecuta el proyecto Pomodoro
    # Se podría hacer un mock para comprobar si el comando fue ejecutado
