proc = int(input("Введите число: "))

for proc in range(21):
    if proc % 10 ==1 and proc % 100 != 11:
        print(proc, "Процент,", end=" ")
    elif 1 < proc % 10 < 5 and not 11 < proc % 100 <15:
        print(proc, "Процента,", end=" ")
    else:
        print(proc, "Процентов,", end=" ")
