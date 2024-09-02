import math as m  

def isSquare(n):  
    s = int(m.sqrt(n))  
    return s * s == n

def isFibonacci(n):  
    return isSquare(5 * n * n + 4) or isSquare(5 * n * n - 4)  
    
numero = int(input("Escolha o numero: "))
if (isFibonacci(numero) == True):  
    print (f"Número {numero}: Sim, o número dado é um Numero de Fibonacci")  
else:  
    print (f"Número {numero}: Não, o número dado não é um Numero de Fibonacci")  
    