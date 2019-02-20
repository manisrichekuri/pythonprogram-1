fact=1
n=int(input())
if n<0:
  print("invalid")
elif n==0:
  print("",1)
else: 
  for i in range(1,n+1):
    fact=fact*i 
  print(fact)     

