import tkinter as tk
from tkinter import ttk

from tkcalendar import DateEntry

from budget_app.helpers.const import LABEL_ORIENTATION, LABEL_PAD_X, \
    LARGE_PAD_Y_TOP, ENTRY_ORIENTATION, LABEL_PAD_Y, BUTTON_ORIENTATION, \
    BUTTON_PAD_X, BUTTON_PAD_Y, COMBO_ORIENTATION
from budget_app.helpers.my_enums import Category, Account, Currency, \
    TransactionType


class TransactionContainer(ttk.Frame):
    """ Code of the LabelFrames """

    def __init__(self, parent):
        super().__init__(parent)

        # ---- Setup grid of GUI ---- #
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=0)
        self.grid_columnconfigure(index=3, weight=0)
        self.grid_columnconfigure(index=4, weight=1)

        # ---- TRANSACTION Widgets ---- #
        # description widget
        self.description_label = ttk.Label(self,
                                           text="Concepto")
        self.description_label.grid(row=0, column=0,
                                    sticky=LABEL_ORIENTATION,
                                    padx=LABEL_PAD_X,
                                    pady=(LARGE_PAD_Y_TOP, 10))
        self.description_input = ttk.Entry(self)
        self.description_input.grid(row=0, column=1,
                                    sticky=ENTRY_ORIENTATION,
                                    padx=LABEL_PAD_X,
                                    pady=(LARGE_PAD_Y_TOP, 10))

        # amount widget
        self.amount_label = ttk.Label(self, text="Monto")
        self.amount_label.grid(row=1, column=0,
                               sticky=LABEL_ORIENTATION,
                               padx=LABEL_PAD_X,
                               pady=LABEL_PAD_Y)
        self.amount_input = ttk.Entry(self)
        self.amount_input.grid(row=1, column=1,
                               sticky=ENTRY_ORIENTATION,
                               padx=LABEL_PAD_X,
                               pady=LABEL_PAD_Y)

        # currency widget
        self.currency_input = ttk.Combobox(self,
                                           values=[Currency.EUR.value,
                                                   Currency.GBP.value,
                                                   Currency.MXN.value])
        self.currency_input.current(0)  # Set EUR as default value
        self.currency_input.grid(row=1, column=2,
                                 sticky=COMBO_ORIENTATION,
                                 padx=LABEL_PAD_X)

        # transaction type widget
        self.transaction_type_label = \
            ttk.Label(self, text="Tipo de transacción")
        self.transaction_type_label.grid(row=2, column=0,
                                         sticky=LABEL_ORIENTATION,
                                         padx=LABEL_PAD_X,
                                         pady=LABEL_PAD_Y)
        self.transaction_type_input = \
            ttk.Combobox(self, values=[TransactionType.INCOME.value,
                                       TransactionType.EXPENDITURE.value])
        self.transaction_type_input.current(0)  # Set INCOME as default value
        self.transaction_type_input.grid(row=2, column=1,
                                         sticky=ENTRY_ORIENTATION,
                                         padx=LABEL_PAD_X,
                                         pady=LABEL_PAD_Y)

        # operation date widget
        self.operation_date_label = ttk.Label(self,
                                              text="Fecha de la operación")
        self.operation_date_label.grid(row=5, column=0,
                                       sticky=LABEL_ORIENTATION,
                                       padx=LABEL_PAD_X,
                                       pady=LABEL_PAD_Y)
        self.operation_date_input = DateEntry(self, selectmode="day",
                                              date_pattern="dd/mm/yyyy")
        self.operation_date_input.grid(row=5, column=1,
                                       sticky=ENTRY_ORIENTATION,
                                       padx=LABEL_PAD_X,
                                       pady=LABEL_PAD_Y)

        self.image = tk.PhotoImage(file="")
        self.image_label = ttk.Label(self, image=self.image)

        # account widget
        self.account_label = \
            ttk.Label(self, text="Cuenta")
        self.account_label.grid(row=6, column=0,
                                sticky=LABEL_ORIENTATION,
                                padx=LABEL_PAD_X,
                                pady=LABEL_PAD_Y)
        self.account_input = \
            ttk.Combobox(self, values=[Account.LCL.value,
                                       Account.BOURSORAMA.value,
                                       Account.CASH.value,
                                       Account.TR.value])
        self.account_input.current(0)  # Set LCL as default value
        self.account_input.grid(row=6, column=1,
                                sticky=COMBO_ORIENTATION,
                                padx=LABEL_PAD_X,
                                pady=LABEL_PAD_Y)

        # category widget
        self.category_label = \
            ttk.Label(self, text="Categoría")
        self.category_label.grid(row=7, column=0,
                                 sticky=LABEL_ORIENTATION,
                                 padx=LABEL_PAD_X,
                                 pady=LABEL_PAD_Y)
        self.category_input = \
            ttk.Combobox(self, values=[Category.FIXED.value,
                                       Category.SAVINGS.value,
                                       Category.DONATIONS.value,
                                       Category.INVESTMENTS.value,
                                       Category.TRANSFERS.value])
        self.category_input.current(0)  # Set FIXED as default value
        self.category_input.grid(row=7, column=1,
                                 sticky=COMBO_ORIENTATION,
                                 padx=LABEL_PAD_X,
                                 pady=LABEL_PAD_Y)

        # note widget
        self.note_label = ttk.Label(self, text="Nota")
        self.note_label.grid(row=8, column=0,
                             sticky=LABEL_ORIENTATION,
                             padx=LABEL_PAD_X,
                             pady=LABEL_PAD_Y)
        self.note_input = tk.Text(self, height=4, width=30)
        self.note_input.grid(row=8, column=1,
                             sticky=ENTRY_ORIENTATION,
                             padx=LABEL_PAD_X,
                             pady=LABEL_PAD_Y)

        # Create button (just for the example)
        self.add_btn = \
            ttk.Button(master=self, text="Ingresar transacción")
        self.add_btn.grid(row=10,
                          column=1,
                          sticky=BUTTON_ORIENTATION,
                          padx=BUTTON_PAD_X,
                          pady=BUTTON_PAD_Y)


class UpdateTransactionContainer(ttk.Frame):
    """ Code of the LabelFrames """

    def __init__(self, parent):
        super().__init__(parent)

        # ---- Setup grid of GUI ---- #
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=0)
        self.grid_columnconfigure(index=3, weight=0)
        self.grid_columnconfigure(index=4, weight=1)

        # ---- TRANSACTION Widgets ---- #
        # description widget
        self.description_label = ttk.Label(self,
                                           text="Concepto")
        self.description_label.grid(row=0, column=0,
                                    sticky=LABEL_ORIENTATION,
                                    padx=LABEL_PAD_X,
                                    pady=(LARGE_PAD_Y_TOP, 10))
        self.description_input = ttk.Entry(self)
        self.description_input.grid(row=0, column=1,
                                    sticky=ENTRY_ORIENTATION,
                                    padx=LABEL_PAD_X,
                                    pady=(LARGE_PAD_Y_TOP, 10))

        # amount widget
        self.amount_label = ttk.Label(self, text="Monto")
        self.amount_label.grid(row=1, column=0,
                               sticky=LABEL_ORIENTATION,
                               padx=LABEL_PAD_X,
                               pady=LABEL_PAD_Y)
        self.amount_input = ttk.Entry(self)
        self.amount_input.grid(row=1, column=1,
                               sticky=ENTRY_ORIENTATION,
                               padx=LABEL_PAD_X,
                               pady=LABEL_PAD_Y)

        # currency widget
        self.currency_input = ttk.Combobox(self,
                                           values=[Currency.EUR.value,
                                                   Currency.GBP.value,
                                                   Currency.MXN.value])
        self.currency_input.current(0)  # Set EUR as default value
        self.currency_input.grid(row=1, column=2,
                                 sticky=COMBO_ORIENTATION,
                                 padx=LABEL_PAD_X)

        # transaction type widget
        self.transaction_type_label = \
            ttk.Label(self, text="Tipo de transacción")
        self.transaction_type_label.grid(row=2, column=0,
                                         sticky=LABEL_ORIENTATION,
                                         padx=LABEL_PAD_X,
                                         pady=LABEL_PAD_Y)
        self.transaction_type_input = \
            ttk.Combobox(self, values=[TransactionType.INCOME.value,
                                       TransactionType.EXPENDITURE.value])
        self.transaction_type_input.current(0)  # Set INCOME as default value
        self.transaction_type_input.grid(row=2, column=1,
                                         sticky=ENTRY_ORIENTATION,
                                         padx=LABEL_PAD_X,
                                         pady=LABEL_PAD_Y)

        # operation date widget
        self.operation_date_label = ttk.Label(self,
                                              text="Fecha de la operación")
        self.operation_date_label.grid(row=5, column=0,
                                       sticky=LABEL_ORIENTATION,
                                       padx=LABEL_PAD_X,
                                       pady=LABEL_PAD_Y)
        self.operation_date_input = DateEntry(self, selectmode="day",
                                              date_pattern="dd/mm/yyyy")
        self.operation_date_input.grid(row=5, column=1,
                                       sticky=ENTRY_ORIENTATION,
                                       padx=LABEL_PAD_X,
                                       pady=LABEL_PAD_Y)

        self.image = tk.PhotoImage(file="")
        self.image_label = ttk.Label(self, image=self.image)

        # account widget
        self.account_label = \
            ttk.Label(self, text="Cuenta")
        self.account_label.grid(row=6, column=0,
                                sticky=LABEL_ORIENTATION,
                                padx=LABEL_PAD_X,
                                pady=LABEL_PAD_Y)
        self.account_input = \
            ttk.Combobox(self, values=[Account.LCL.value,
                                       Account.BOURSORAMA.value,
                                       Account.CASH.value,
                                       Account.TR.value])
        self.account_input.current(0)  # Set LCL as default value
        self.account_input.grid(row=6, column=1,
                                sticky=COMBO_ORIENTATION,
                                padx=LABEL_PAD_X,
                                pady=LABEL_PAD_Y)

        # category widget
        self.category_label = \
            ttk.Label(self, text="Categoría")
        self.category_label.grid(row=7, column=0,
                                 sticky=LABEL_ORIENTATION,
                                 padx=LABEL_PAD_X,
                                 pady=LABEL_PAD_Y)
        self.category_input = \
            ttk.Combobox(self, values=[Category.FIXED.value,
                                       Category.SAVINGS.value,
                                       Category.DONATIONS.value,
                                       Category.INVESTMENTS.value,
                                       Category.TRANSFERS.value])
        self.category_input.current(0)  # Set FIXED as default value
        self.category_input.grid(row=7, column=1,
                                 sticky=COMBO_ORIENTATION,
                                 padx=LABEL_PAD_X,
                                 pady=LABEL_PAD_Y)

        # note widget
        self.note_label = ttk.Label(self, text="Nota")
        self.note_label.grid(row=9, column=0,
                             sticky=LABEL_ORIENTATION,
                             padx=LABEL_PAD_X,
                             pady=LABEL_PAD_Y)
        self.note_input = tk.Text(self, height=4, width=30)
        self.note_input.grid(row=9, column=1,
                             sticky=ENTRY_ORIENTATION,
                             padx=LABEL_PAD_X,
                             pady=LABEL_PAD_Y)

        # Create button (just for the example)
        self.update_btn = \
            ttk.Button(master=self, text="Actualizar transacción")
        self.update_btn.grid(row=10,
                             column=1,
                             sticky=BUTTON_ORIENTATION,
                             padx=BUTTON_PAD_X,
                             pady=BUTTON_PAD_Y)


class TagContainer(ttk.Frame):
    """ Code of the LabelFrames """

    def __init__(self, parent):
        super().__init__(parent)

        # ---- Setup grid of GUI ---- #
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=0)
        self.grid_columnconfigure(index=3, weight=0)
        self.grid_columnconfigure(index=4, weight=1)

        # ---- TAG Widgets (labels, entries, buttons...) ---- #
        # name widget
        self.name_label = ttk.Label(self, text="Etiqueta")
        self.name_label.grid(row=11, column=0,
                             sticky=LABEL_ORIENTATION,
                             padx=LABEL_PAD_X,
                             pady=(LARGE_PAD_Y_TOP, 0))
        self.name_input = ttk.Entry(self)
        self.name_input.grid(row=11, column=1,
                             sticky=ENTRY_ORIENTATION,
                             padx=LABEL_PAD_X,
                             pady=(LARGE_PAD_Y_TOP, 0))

        # Create button (just for the example)
        self.add_tag_button = \
            ttk.Button(master=self, text="Ingresar etiqueta")
        self.add_tag_button.grid(row=12,
                                 column=1,
                                 sticky=BUTTON_ORIENTATION,
                                 padx=BUTTON_PAD_X,
                                 pady=BUTTON_PAD_Y)
