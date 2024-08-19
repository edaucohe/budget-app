import tkinter as tk
from tkinter import ttk

from budget_app.helpers.const import APP_NAME, WIDTH, HEIGHT
from budget_app.views.frames import TransactionFrame, TagFrame, BudgetFrame
# from budget_app.views.tabs import Tabs


class GUISetup(tk.Tk):
    def __init__(self, app_name, width, height):
        super().__init__()
        min_width = int(width / 2)
        min_height = int(height / 2)

        max_width = self.winfo_screenwidth()
        max_height = self.winfo_screenheight()

        # Window setup
        self.title(app_name)
        # self.geometry(f"{width}x{height}")
        # self.geometry("%dx%d+0+0" % (max_width, max_height))
        self.geometry(f"{max_width}x{max_height}")
        self.minsize(min_width, min_height)


class Tabs(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        # Transaction tab
        self.transaction_tab = TransactionFrame(self)
        self.transaction_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.transaction_tab, text="Transacciones")

        # Tag tab
        self.tag_tab = TagFrame(self)
        self.tag_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.tag_tab, text="Etiquetas")

        # Budget tab
        self.budget_tab = BudgetFrame(self)
        self.budget_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.budget_tab, text="Presupuesto")


class GUIView:
    def __init__(self):
        self.gui_setup = GUISetup(APP_NAME, WIDTH, HEIGHT)

        # Tabs
        self.gui_setup.tabs = Tabs(self.gui_setup)
        self.gui_setup.tabs.pack(side="top", fill="x")

    def run_mainloop(self):
        self.gui_setup.mainloop()
