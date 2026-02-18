def even_number(a,b,c):
    count=0
    if a%2==0:
        count+=1
    if b%2==0:
        count+=1
    if c%2==0:
        count+=1
    return count
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))
result=even_number(a,b,c)
print("count of even numbers:",result)
