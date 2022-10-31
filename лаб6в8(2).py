l=[float(input()) for i in range(1,5)]#про длинну массива ничего в задании нет
sr=sum(l)/len(l)
for i in range(0,4):
    if l[i]==0:
        l[i]=sr
print(l)
