# How I Answer the exercise
data = open("2024/input_1.txt", "r").read()
data = data.split('\n')
data = [x.split("   ") for x in data]
int_data =  [[int(x) for x in y] for y in data if y != ['']]
list_0,list_1 = zip(*int_data)
list_0 = list(list_0)
list_1 = list(list_1)
list_0 = sorted(list_0)
list_1 = sorted(list_1)
distance = 0
for n in range(len(list_0)):
    distance += abs(list_0[n] - list_1[n])

print(distance)

###### Other better ways 1 - Using arrays 
# import numpy as np
# # Convert to numpy arrays
# array_0, array_1 = zip(*data)  # Unpack into two lists of strings
# array_0 = np.array(array_0, dtype=int)  # Convert list to numpy array of integers
# array_1 = np.array(array_1, dtype=int)

# # Sort both arrays
# array_0 = np.sort(array_0)
# array_1 = np.sort(array_1)

# # Calculate the distance
# distance = np.sum(np.abs(array_0 - array_1))  # Efficient element-wise subtraction

# print(distance)

###### Other better ways 2 - Summary distance function through list comprehensino
# distance = sum(abs(x - y) for x, y in zip(sorted(list_0), sorted(list_1)))

###### Other better ways 3 - Int using map
# list_0, list_1 = zip(*data)  # Use 'data' instead of 'int_data'
# list_0 = list(map(int, list_0))
# list_1 = list(map(int, list_1))

