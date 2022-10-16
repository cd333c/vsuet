l=[float(input()) for i in range(1,4)]#про длинну массива ничего в задании нет
print("Сумма равна ",sum(l))
pr=1
for i in range(0,3):
    pr=pr*l[i]
print("Произведение равно ",pr)
