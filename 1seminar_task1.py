# За день машина проезжает n километров. Сколько 
# дней нужно, чтобы проехать маршрут длиной m 
# километров? При решении этой задачи нельзя 
# пользоваться условной инструкцией if и циклами.

n = int(input('Сколько км машина проезжает за день? '))
m = int(input('Длина маршрута? '))

print(int((m-1)/n)+1)