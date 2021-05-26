#In order to check the number is prime or not.   
import math  
   
def prime_check(x):
    if x > 1:
        z=int(math.sqrt(x))
        for i in range(2,z+1):
            if x%i!=0:
                continue 
            else:
                return str(x) +' is not a prime number'
                break
    else:
        return str(x) +' is not a prime number'
        
    return str(x) +' is a prime number'        
        
      
