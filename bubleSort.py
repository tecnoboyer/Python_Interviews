# This is  the BUBLE SORT ALGORITHM
# First get the user array



# Step 1: Get the number of elements in the array
num_elements = int(input("Enter the number of elements: "))

# Step 2: Initialize an empty list to store the integers
array = []

# Step 3: Use a loop to fill the array with integers
for i in range(num_elements):
    try:
        # Read an integer from the user
        value = int(input(f"Enter element {i + 1}: "))
        
        # Append the integer to the list
        array.append(value)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Step 4: Print the filled array
print("The array is:", array)


# Now the Buble Sort

for s in range (len(array)):
    for t in range(len(array)-s-1):
        if array[t+1]<array[t]:
            temp=array[t]
            array[t]=array[t+1]
            array[t+1]=temp
print(array)




