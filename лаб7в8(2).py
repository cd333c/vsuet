for i in range(1, int(input()) + 1):
     k=True
     for e in str(i):
         if e == '0' or i%int(e):
             k= False
     if k:
        print(i)
