print("Enter the number of prime numbers you want :")

try: 
    n=2
    flag=0
    i=3
    value=int(input())
    print("PROCESANDO")
    print("Prime is : 2")
    while( n<=value):

        for j in range(2,i):
            if(i%j==0):
                flag=0
                break
            else:
                flag=1
        if(flag==1):
            print("Prime is : 2",i)
            flag==0
            n=n+1   # if the number is prime so you indicate that the while cicle end succesfully
        else:
            n=n  # if the number 
        i=i+1

except:
    print("Data entered is not a number")

