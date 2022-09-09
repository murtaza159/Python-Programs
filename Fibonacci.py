nterms = int(input ("Enter number of terms: "))  

n1 = 0  
n2 = 1  
count = 0  
   


if nterms == 1:  
    print ("The Fibonacci sequence of the numbers up to", nterms, ": ")  
    print(n1)  

else:  
    print ("Fibonacci sequence: ")  
    while count < nterms:  
        print(n1)  
        nth = n1 + n2  

        n1 = n2  
        n2 = nth  
        count += 1  