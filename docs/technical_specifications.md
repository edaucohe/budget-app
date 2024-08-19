# Especificaciones técnicas

## Tecnologías
Las tecnologías a utilizar son:
- Python
- Tkinter (interfaz gráfica de escritorio)

## Requisitos técnicos
Los requisitos técnicos son:
- POO
-  

## Modelos
Hay 2 modelos:
- Transaction
- Tag

### Model "Transaction"
Estos son los atributos del modelo "Transaction":


| #   |    Atributo    |  Tipo de dato   |               Descripción                | ¿Requisito?  |
|-----|:--------------:|:---------------:|:----------------------------------------:|:------------:|
| 1   |  description   |       str       |        Concepto de la transacción        |      Sí      |
| 2   |     amount     |      float      |         Monto de la transacción          |      Sí      |
| 3   |      type      | TransactionType |          Si es ingreso o gasto           |      Sí      |
| 4   |    account     |     Account     |  Tipo de cuenta (banco, efectivo, etc.)  |      Sí      |
| 5   | operation_date |      date       |         Fecha de la transacción          |      Sí      |
| 6   |    category    |    Category     |   (donación, ahorro, gasto fijo, etc.)   |      Sí      | 
| 7   |    currency    |    Currency     |              Divisa (euros)              |      Sí      |
| 8   |      tag       |       Tag       | (alimentación, transporte, viajes, etc.) |      No      |
| 9   |      note      |       str       |              Nota adicional              |      No      |


### Model "Tag"

