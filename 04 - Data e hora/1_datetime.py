from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(date.today())


data_hora = datetime(2023, 7, 10) # o idela é colocar o valor de horas, caso não seja preenchido ficará zerado
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)
print(hora)
