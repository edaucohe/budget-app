from typing import Optional

from budget_app.helpers.tags_saved import get_tags
from budget_app.models import Transaction, Tag
from budget_app.views.gui_setup import GUIView


class Controller:
    def __init__(self,
                 transaction: Optional[Transaction] = None,
                 tag: Optional[Tag] = None,
                 view: Optional[GUIView] = None,
                 ):
        self.transaction = transaction or Transaction
        self.tag = tag or Tag
        self.view = view or GUIView()

        self.transaction_tab = self.view.gui_setup.tabs.transaction_tab
        self.add_transaction_btn = \
            self.transaction_tab.add_transaction_container.add_btn
        self.update_transaction_btn = \
            self.transaction_tab.update_transaction_container.update_btn

        # Tag widgets
        self.tag_tab = self.view.gui_setup.tabs.tag_tab
        self.add_tag_btn = \
            self.tag_tab.tag_container.add_tag_btn
        self.tags = []

        # self.send_tags()

        self.bind()  # To call bind method

    def bind(self):
        # Link buttons of TRANSACTION TAB
        self.add_transaction_btn.config(command=self.get_transaction_data)
        self.update_transaction_btn.config(command=self.update_transaction_data)

        # Link buttons of TAG TAB
        self.add_tag_btn.config(command=self.get_tag_data)

    # ---- TRANSACTION methods ---- #
    def get_transaction_data(self):
        # TODO Code to get Transaction data
        print("Button ADD TRANSACTION clicked!")
        print(self.add_transaction_btn)

        user_data = {
            "description": self.transaction_tab.add_transaction_container.description_input.get(),
            "amount": self.transaction_tab.add_transaction_container.amount_input.get(),
            "operation_date": self.transaction_tab.add_transaction_container.operation_date_input.get(),
            "category": self.transaction_tab.add_transaction_container.category_input.get(),
            "transaction_type": self.transaction_tab.add_transaction_container.transaction_type_input.get(),
            "account": self.transaction_tab.add_transaction_container.account_input.get(),
            "currency": self.transaction_tab.add_transaction_container.currency_input.get(),
            "note": self.transaction_tab.add_transaction_container.note_input.get('1.0', 'end-1c'),  # (end-1c discard the automatically added newline at the end).
        }

        print("Transaction USER DATA: ", user_data)
        transaction_deserialized = self.transaction.deserialize(user_data)
        print("Transaction DESERIALIZED: ", transaction_deserialized)

    def update_transaction_data(self):
        # TODO Code to get Transaction data
        print("Button UPDATE TRANSACTION clicked!")
        print(self.update_transaction_btn)

    # ---- TAG methods ---- #
    # TODO Code to get Tag data
    def get_tag_data(self):
        print("Button TAG clicked!")
        user_data = {
            "name": self.tag_tab.tag_container.name_input.get(),
        }
        print("Tag USER DATA: ", user_data)

        tag_deserialized = self.tag.deserialize(user_data)
        # self.tag.list_tags(tag_deserialized)
        self.tags.append(tag_deserialized)
        print("Tag DESERIALIZED: ", tag_deserialized)
        # print("tags: ", self.tags)

    # def send_tags(self):
    #     get_tags(self.tags)

    def run(self):
        self.view.run_mainloop()
