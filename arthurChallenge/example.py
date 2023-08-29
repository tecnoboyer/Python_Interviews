
input_str = input("Enter a list of numbers separated by commas: ")
number_str_list = input_str.split(',')
number_list = [int(num) for num in number_str_list]
acu=0
acu2=0
result=0
for element in number_list:
    acu=0
    for dig in str(element):
        acu=acu+int(dig)
        
    if(acu2>acu):
        result=acu2
    else:
        result=acu
print(result)




# print("List of numbers:", number_list)
