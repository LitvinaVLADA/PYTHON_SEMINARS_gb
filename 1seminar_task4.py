# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов 
# сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input('Количество сделанных журавликов: '))

if s%2 == 0:
    k = s//2
    ps = k//2
else:
    k = s//2
    ps = k//2+1  

print('Катя сделала ', k,' журавликов, а Петя и Серёжа сделали по ', ps,' журавликов каждый.')