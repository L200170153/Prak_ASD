def segiEmpat(x,y):
    for i in range(y):
        if i==0 or i==y-1:
            print("@"*x)
        else:
            print("@"+" "*(x-2)+"@")

segiEmpat(5,10)
