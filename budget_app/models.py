from datetime import date
from typing import Optional, Dict

from budget_app.helpers.my_enums import \
    TransactionType, Account, Category, Currency


class Tag:
    def __init__(self,
                 name: str,
                 image: Optional[str] = None):
        self.name = name
        self.image = image


class Transaction:
    def __init__(self,
                 description: str,
                 amount: float,
                 operation_date: date,
                 category: Category,
                 transaction_type: TransactionType,
                 account: Account,
                 currency: Currency = Currency.EUR,
                 tag: Optional[Tag] = None,
                 note: Optional[str] = "",
                 ):
        self.description = description
        self.amount = amount
        self.type = transaction_type
        self.account = account
        self.operation_date = operation_date
        self.category = category
        self.currency = currency
        self.tag = tag
        self.note = note

    # def __repr__(self):
    #     return f"Transaction(description={self.description})"

    @classmethod
    def deserialize(cls, transaction_data: Dict[str, str]) -> 'Transaction':
        data = dict()
        data["description"] = transaction_data["description"]
        data["amount"] = cls.to_float(transaction_data["amount"])
        data["currency"] = Currency(transaction_data["currency"])
        data["transaction_type"] = \
            TransactionType(transaction_data["transaction_type"])
        data["operation_date"] = \
            cls.to_date(transaction_data["operation_date"])
        data["account"] = Account(transaction_data["account"])
        data["category"] = Category(transaction_data["category"])
        data["note"] = transaction_data["note"]

        print("data from MODEL: ", data)

        return cls(**data)

    @staticmethod
    def to_float(amount):
        if amount.replace(".", "").isnumeric():
            return float(amount)
        else:
            print("Amount is not a float")
            return 0

    @staticmethod
    def to_date(date_as_str):
        if date_as_str == "":
            print("There is no date")
            return date.today()
        else:
            new_date = date_as_str.split("/")
            new_date.reverse()
            new_date = "-".join(new_date)
            return date.fromisoformat(new_date)
