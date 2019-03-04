def tesPrima(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                print(x," bukan bilangan prima")
                break
            else:
                print(x," bilangan prima")
                break
    else:
        print(x, " bukan bilangan prima")
        
for i in range(2,1001):
    tesPrima(i)
    

    
