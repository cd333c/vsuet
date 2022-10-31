import copy
def tr(matrix):
    for i in range(n):
        for j in range(n):
            matrix[i][j]=a[j][i]
    return matrix
def printfm(A):
    for row in A:
        for elem in row:
            print(elem, end = ' ')
        print()
n=int(input("Введите n:"))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print("Введите элемент [{}],[{}]".format(i,j))
        b.append(int(input()))
    a.append(b)
b=copy.deepcopy(a)
print("Начальная матрица:")
printfm(a)
print("Транспорированная матрица:")
printfm(tr(b))
