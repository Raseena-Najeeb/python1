import random
n = random.randint(1,100)
a=input("any number between 1 and 100")
if(a==n):
    print('you are correct')
else:
 b= input("try again")

if(b==n):
    print('you are correct')
else:
 c= input("try again")
if(c==n):
    print('you are correct')
else:
 d= input("try again")
 
if(d==n):
    print('you are correct')
else:
 e= input("try again")
if(e==n):
    print('you are correct')
else:
 print("you lost")
 print("answer is")
 print(n)