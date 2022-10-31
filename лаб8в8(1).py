def printfm(A):
    for row in A:
        for elem in row:
            print(elem, end = ' ')
        print()
n=int(input("Введите n:"))
k=int(input("Введите k:"))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print("Введите элемент [{}],[{}]".format(i,j))
        b.append(int(input()))
    a.append(b)
print("Насальная матрица:")
printfm(a)
for j in range(n):
    a[k-1][j]/=a[k-1][k-1]
print("Преобразованная матрица:")
printfm(a)
