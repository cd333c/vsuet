def change1(mas):
    e1=mas[0]
    el=mas[len(mas)-1]
    mas[0]=el
    del mas[len(mas)-1]
    mas.append(e1)
    return mas
A=[]

for i in range(0,int(input("Введите длинну мвссива:\n"))):
    print("Введите",i+1,"элемент массива")
    A.append(input())
print(A)
print(change1(A))

    
