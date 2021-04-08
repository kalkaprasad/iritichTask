

def nextNumber(ls,siz):
    diff=0
    fis= ls[0]
    diff= ls[siz-1]-(ls[siz-2])
    mainvalue= diff+ls[siz-1]

    return  mainvalue


# Enter the List   Value
ls=[3, 10, 15, 26, 35, 50, 63] # this is  the List of the List of Series
siz= len(ls) # this is the Size of the  len..
ans=nextNumber(ls,siz)
print(ans)