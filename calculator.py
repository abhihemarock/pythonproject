def add():
     print("enter values of a,b")
     a=int(input())
     b=int(input())
     print(a+b)
def sub():
     print("enter values of a,b")
     a=int(input())
     b=int(input())
     print(a-b)
def mul():
     print("enter values of a,b")
     a=int(input())
     b=int(input())
     print(a*b)
def div():
     print("enter values of a,b")
     a=int(input())
     b=int(input())
     print(a/b)
def mod():
     print("enter values of a,b")
     a=int(input())
     b=int(input())
     print(a%b)   
print("enter your choice")
print("1.addition\n","2.subtraction\n","3.multiplication\n","4.division\n","5.modules")
a=int(input())
if a == 1 :
    add()
elif a== 2:
     sub()
elif a==3:
    mul()
elif a==4:
    div()
elif a==5:
    mod()
