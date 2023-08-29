
fWord=str(input())

long=len(fWord)
j=long-1
flag=0

for i in range(long):
    if (fWord[i]==fWord[j]):
        j=j-1
        flag=1
    else:
        flag=0
        break

if(flag==0):
    print("word is no a capicuous")
else:
    print("EUREKA you has found a CAPICUOUS! ")
    



