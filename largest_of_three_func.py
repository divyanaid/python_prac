#largest of three numbers using functions
def largest_num(a,b,c):
    if a >=b and a >=c:
        return a
    elif b >=a and b >=c:
        return b
    else:
        return c
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
largest=largest_num(a,b,c)
print("largest num is:",largest)
