from tkinter import ttk

from budget_app.views.containers import TransactionContainer, TagContainer, \
    UpdateTransactionContainer


class TransactionFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # ---- Frame grid configuration ---- #
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)

        # ---- LABEL FRAMES ---- #
        # ADD TRANSACTION container
        self.add_transaction_label_frame = \
            ttk.LabelFrame(self, text="Ingresar transacción")
        self.add_transaction_label_frame.grid(row=0, column=0,
                                              sticky="nsew",
                                              padx=10,
                                              pady=(20, 0))

        # Display widgets of ADD TRANSACTION container
        self.add_transaction_container = \
            TransactionContainer(self.add_transaction_label_frame)
        self.add_transaction_container.grid(row=0, column=0, sticky="nsew")

        # UPDATE TRANSACTION container
        self.update_transaction_label_frame = \
            ttk.LabelFrame(self, text="Actualizar transacción")
        self.update_transaction_label_frame.grid(row=0, column=1,
                                                 sticky="nsew",
                                                 padx=10,
                                                 pady=(20, 0))

        self.update_transaction_container = \
            UpdateTransactionContainer(self.update_transaction_label_frame)
        self.update_transaction_container.grid(row=0, column=1, sticky="nsew")


class TagFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # ---- Frame grid configuration ---- #
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)

        # ---- LABEL FRAMES ---- #
        # Tag container
        self.tag_label_frame = \
            ttk.LabelFrame(self, text="Ingresar etiqueta")
        self.tag_label_frame.grid(row=0, column=0,
                                  sticky="nsew",
                                  pady=(20, 0))

        self.tag_container = \
            TagContainer(self.tag_label_frame)
        self.tag_container.grid(row=0, column=1, sticky="nsew")


class BudgetFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # ---- Frame grid configuration ---- #
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)

        # ---- LABEL FRAMES ---- #
        # BUDGET container
        self.budget_label_frame = \
            ttk.LabelFrame(self, text="Presupuesto")
        self.budget_label_frame.grid(row=0, column=0,
                                     sticky="nsew",
                                     pady=(20, 0))

        # self.budget_container = \
        #     BudgetContainer(self.budget_label_frame)
        # self.budget_container.grid(row=0, column=1, sticky="nsew")
