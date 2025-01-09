import tkinter as tk
from tkinter import messagebox
from services.project_service import ProjectService

class CentralAppUI:
    def __init__(self, root, project_service):
        self.root = root
        self.project_service = project_service

        self.root.title("Centralizador de Proyectos")
        self.root.geometry("400x300")

        self.create_ui()

    def create_ui(self):
        self.project_listbox = tk.Listbox(self.root, height=10, width=30)
        self.project_listbox.pack(pady=20)

        self.refresh_button = tk.Button(self.root, text="Refrescar Proyectos", command=self.refresh_projects)
        self.refresh_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="Ejecutar Proyecto", command=self.execute_selected_project)
        self.run_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.quit_button.pack(pady=5)

        self.refresh_projects()

    def refresh_projects(self):
        self.project_listbox.delete(0, tk.END)
        projects = self.project_service.list_projects()
        for project in projects:
            self.project_listbox.insert(tk.END, project)

    def execute_selected_project(self):
        selected_project = self.project_listbox.get(tk.ACTIVE)
        if selected_project:
            try:
                self.project_service.execute_project(selected_project)
                messagebox.showinfo("Éxito", f"Proyecto {selected_project} ejecutado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo ejecutar el proyecto {selected_project}. Error: {e}")
        else:
            messagebox.showwarning("Selección inválida", "Selecciona un proyecto para ejecutar.")
