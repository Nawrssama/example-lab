def Fibonacci(n):
    if n == 0 :
        return(0)
    if n == 1 :
        return(1)
    if n > 1 :
        return(Fibonacci(n-1)+Fibonacci(n-2))
    
def Lucas(n):
    if n == 0 :
        return(2)
    if n == 1 :
        return(1)
    if n > 1 :
        return(Lucas(n-1)+Lucas(n-2))
