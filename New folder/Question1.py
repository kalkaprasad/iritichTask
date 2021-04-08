# First Question ..
# Math methical function

def soltution(i,x):

    return (1/x*i)

def equation(i,x):
    res=0;
    if(i==1):
        return  1
    else:
        return soltution(equation(i-1,x),x)




i = int(input("Enter The Value of I"))
x= int(input("Enter The value of X"))
a= equation(i,x)

print(a)
