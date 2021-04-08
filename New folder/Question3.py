
def questionmath(x, y, a, b ):
    ans=0;
    try:
        ans = (x + pow(1 / y, a)) * (x - pow(1 / y, b)) / (y + pow(1 / x, a)) * (y - pow(1 / x, b))
    except:
        print("division by zero Exception ")

    return  ans
x= int(input())
y= int(input())
a= int(input())
b= int(input())
aa=questionmath(x, y, a, b )
print(aa)
