n = int(input('enter number: '))
a = 0
number = 0
for i in range(n+1):
    a = a + i
    number = number + 1
average = a / number
print(f' average = {average}')