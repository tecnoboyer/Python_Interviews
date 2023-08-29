

n=int()
flag1=bool(False)
flag2=bool(False)

for n in range (1,100):
    if(n%3==0):
        flag1=True
    if(n%5==0):
        flag2=True
    if(flag1):
        if(flag2):
            print("FizzBuzz :", n)
            flag1=False
            flag2=False
        else:
            print("Fizz:", n)
            flag1=False
            flag2=False
    if(flag2):
        if(flag1):
            print("FizzBuzz:", n)
            flag1=False
            flag2=False
        else:
            print("Buzz:", n)
            flag1=False
            flag2=False

    