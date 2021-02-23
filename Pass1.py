duration = int(input("Ведите время в секундах: "))
sec = duration % 60
minute = duration // 60 % 60
hour = duration // 3600 - duration // 3600 // 24 * 24
days = duration // 3600 // 24
month = days // 30 % 30
year = month // 12 % 12
century = year // 100 % 100

print("Дней: ", days, ",", "Часов: ", hour, ",", "Минут: ", minute, ",", "Секунд: ", sec, ",", "Месяцев: ", month, ",", "Лет: ", year, ",", "Веков: ", century,".", sep="" )