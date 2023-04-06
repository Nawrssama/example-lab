# all the function


def Fibonacci (n):
    if n == 0 :
        return(0)
    if n == 1 :
        return(1)
    if n > 1 :
        return(Fibonacci(n-1)+Fibonacci(n-2))
    

    
def Lucas (n):
    if n == 0 :
        return(2)
    if n == 1 :
        return(1)
    if n > 1 :
        return(Lucas(n-1)+Lucas(n-2))
    
def sum_series (n,a=0,b=1):
   if a==0 and b==1:
      return Fibonacci(n)
   elif a==2 and b==1:
      return Lucas(n)
   else:
      if n==0:
         return a
      elif n ==1:
         return b
      else:
         return sum_series(n-1,a,b) + sum_series(n-2,a,b)        

    

