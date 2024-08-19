from enum import Enum


class TransactionType(Enum):
    INCOME = "Ingreso"
    EXPENDITURE = "Gasto"


class Account(Enum):
    LCL = "LCL"
    BOURSORAMA = "Boursorama"
    CASH = "Efectivo"
    TR = "Ticket de restauration"


class Currency(Enum):
    EUR = "Euros"
    GBP = "Libras"
    MXN = "Pesos"


class Category(Enum):
    FIXED = "Gastos fijos"
    SAVINGS = "Ahorros"
    DONATIONS = "Donativos"
    INVESTMENTS = "Inversiones"
    TRANSFERS = "Transferencias"
