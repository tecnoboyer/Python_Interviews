# Determinate if a number is prime

print("Enter your value: ")
try:
    val = int(input())
    flag=0

    for i in range (2,val-1):
        if (val%i==0):
            flag=2
            break
        else: flag=1
    if(flag==2):
        print (" Is not a prime")
    if(flag==1):
        print (" Is a prime")
        

except:
    print("Please enter a number")