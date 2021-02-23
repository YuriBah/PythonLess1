my_list_cube = []
list_cubes = []
sum = 0

for i in range(1, 1001, 2):
    my_list_cube.append(i ** 3)

for index,vall in enumerate(my_list_cube):
    all_sum = 0
    while vall > 0:
        all_sum += vall % 10
        vall //= 10
    if all_sum % 7 == 0:
        sum += my_list_cube[index]

print(sum)

for q in my_list_cube:
    list_cubes.append(q + 17)

sum = 0

for index,vall in enumerate(my_list_cube):
    all_sum = 0
    while vall > 0:
        all_sum += vall % 10
        vall //= 10
    if all_sum % 7 == 0:
        sum += my_list_cube[index]

print(sum)







