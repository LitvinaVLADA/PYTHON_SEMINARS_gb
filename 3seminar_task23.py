# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером) 

numb_list = list(map(int, input("Введите числа через пробел: ").split()))
result = 0

for i in range(len(numb_list)-1):
    c_num = numb_list[i]
    n_num = numb_list[i+1]
    if n_num > c_num:
        result += 1
    i += 1 

print('Количество элементов массива, больше предыдущего ', result)