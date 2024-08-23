import datetime
from datetime import date
from typing import Optional, Dict

from budget_app.helpers.my_enums import \
    TransactionType, Account, Category, Currency


class Tag:
    def __init__(self,
                 name: str = "",
                 image: Optional[str] = None):
        self.name = name
        # self.tags = []
        # self.image = image

    def __repr__(self):
        return f"Tag(name={repr(self.name)})"

    @classmethod
    def deserialize(cls, tag_data: Dict[str, str]) -> 'Tag':
        data = dict()
        data["name"] = tag_data["name"]
        print("data from MODEL: ", data)
        return cls(**data)

    # def list_tags(self, new_tag):
    #     self.tags.append(new_tag)

    # def get_tags(self):
    #     return self.tags


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
        self.operation_date = operation_date
        self.category = category
        self.transaction_type = transaction_type
        self.account = account
        self.currency = currency
        self.tag = tag
        self.note = note

    def __repr__(self):
        return f"Transaction(" \
               f"description={repr(self.description)}, " \
               f"amount={repr(self.amount)}, " \
               f"operation_date={repr(self.operation_date)}, " \
               f"category={repr(self.category)}, " \
               f"transaction_type={repr(self.transaction_type)}, " \
               f"account={repr(self.account)}, " \
               f"currency={repr(self.currency)}, " \
               f"tag={repr(self.tag)}, " \
               f"note={repr(self.note)})"

    @classmethod
    def deserialize(cls, transaction_data: Dict[str, str]) -> 'Transaction':
        data = dict()
        data["description"] = transaction_data["description"]
        data["amount"] = cls.to_float(transaction_data["amount"])
        data["operation_date"] = \
            cls.to_date(transaction_data["operation_date"])
        data["category"] = Category(transaction_data["category"])
        data["transaction_type"] = \
            TransactionType(transaction_data["transaction_type"])
        data["account"] = Account(transaction_data["account"])
        data["currency"] = Currency(transaction_data["currency"])
        data["tag"] = ""
        data["note"] = transaction_data["note"]

        print("data from MODEL: ", data)

        return cls(**data)

    @staticmethod
    def to_float(amount):
        if amount.replace(".", "").isnumeric():
            return float(amount)
        else:
            print("Amount is not a float")
            return float(0)

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
