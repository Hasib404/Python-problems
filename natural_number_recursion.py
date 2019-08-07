def func(q):
   if q>=1:
      func(q-1)
      print(q,end=' ')
x=int(input("enter a number"))
func(x)