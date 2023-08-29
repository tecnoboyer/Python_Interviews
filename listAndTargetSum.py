# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.



x = [2,7,11,15] # list
tarjet=9

long=len(x)
j=int()

for i in range(0,long-1):
    for j in range (0,long-1):
        if(i!=j):
            if((x[i]+x[j])==tarjet):
               print( i , j )
               break
    break

