# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def max_sum_pair(arr, target):
    left=0
    sum,sumAc=-int(),-1
    pivot=1
    solut=[-1,-1]
    for i in range(0,len(arr)):
        for j in range (1,len(arr)):
            sum=arr[i]+arr[j]
            if (sum<=target and sum>sumAc and j>i ):
                solut=[arr[i],arr[j]]
                sumAc=sum
            j=+1
        i=+1
        print(solut)
    if(solut[0]>solut[1]):
        solut[0],solut[1]=solut[1],solut[0]
    print("At the end : ",solut)


max_sum_pair([5, 4, 10,3,2], 12)