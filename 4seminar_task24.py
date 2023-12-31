# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

q_bush = int(input('Введите количество кустов: '))

lst = []
for i in range(q_bush):
    value = int(input("Введите количество ягод выросших на кусте номер {}: ".format(i+1)))
    lst.append(value)
    i += 1

ber_sum = 0  # Текущая сумма собранных ягод
max_ber_sum = 0  # Максимальная сумма собранных ягод

for i in range(1, q_bush - 1):
    t = int(lst[i])
    p = int(lst[i-1])
    s = int(lst[i+1])
    ber_sum = t+p+s
    if ber_sum > max_ber_sum:
        max_ber_sum = ber_sum


print('Максимальное количество собранных ягод за один заход собирающий модуль равняется ', max_ber_sum)

