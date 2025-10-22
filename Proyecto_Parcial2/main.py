#pip install -r requirements.txt
import tkinter as tk
from tkinter import messagebox
from login_viw import LoginApp
from  dashboart_viw import DashboardApp

def main():
    root = tk.Tk()
    app = LoginApp(root)
    apps = DashboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
        