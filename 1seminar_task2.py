# Найдите сумму цифр трехзначного числа. 

n = int(input('Введите трёхзначное число: '))
sum = 0 

while n>0:
    sum = sum + (n%10)
    n //= 10

print(sum)