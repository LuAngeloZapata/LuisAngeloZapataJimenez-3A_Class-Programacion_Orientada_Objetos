import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales 
from dashboart_viw import DashboardApp

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        # Encabezado
        tk.Label(root, text="Bienvenido al sistema", font=("Arial", 16, "bold")).pack(pady=16)
        
        # Campos de texto
        tk.Label(root, text="Ingresa tu nombre de usuario:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)
        
        tk.Label(root, text="Ingresa tu contraseña:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)
        
        # Botón
        tk.Button(root, text="Iniciar sesión", command=self.login).pack(pady=20)
        
    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        # Validar campos vacíos
        if not usuario or not password:
            messagebox.showinfo("Datos faltantes", "Por favor ingresa usuario y contraseña.")
            return

        # Validar credenciales usando auth_controller.py
        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso permitido", f"Bienvenido, {usuario}!")
            self.root.destroy() 
            dashboard_root = tk.Tk()
            dashboard_app = DashboardApp(dashboard_root, usuario)
            dashboard_root.mainloop()
        else:
            messagebox.showerror("Acceso denegado", "Tus datos son incorrectos.")

     


# Ejecutar la app
root = tk.Tk()
app = LoginApp(root)
root.mainloop()