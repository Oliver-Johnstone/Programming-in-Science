# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    numbers=list(set(numbers))
# sorts the list in increasing order
    numbers.sort()
    return numbers
numbers=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
#remove duplicate numbers from sorted list
print(remove_duplicates_and_sort(numbers))

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result=[]
    total=0
    for num in arr:
# adds num to total to create new total
        total += num
# adds each total to result list
        result.append(total)
    return result
arr=[1,1,1,1,1]
print(cumulative_sum(arr))

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    output = []
    for i in range(len(lst)):
# checks if the order of the number is a multiple of the step
        if i % step == 0:
            output.append(lst[i])
    return output
lst=[1,3,2,4,3,5,4,6,5]
step=2
print(slice_every_nth(lst, step))
# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    multiply_list = [a*b for a, b in zip(list1, list2)]
# adds the two products from the previous step
    dot_product_list = sum(multiply_list)
    return dot_product_list
list1=[2,3,4]
list2=[4,3,2]
print(dot_product(list1, list2))

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    # Create two lists for the matrices W and Z
    matrix1 = [[13,4,5],
    [2,-9,7],
    [7,3,19]]
    matrix2 = [[2,1,5],
    [3,7,9],
    [-1,13,19]]
# create a result matrix with zeros initially
    result = [[0,0,0],
               [0,0,0],
               [0,0,0]]
# calculate each element of the result matrix 
# the i and j for loops are used to go element by element
# the k for loop is used to calculate the product to be stored at each position in the result.
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):  
            for k in range(len(matrix1)):
               result[i][j] += matrix1[i][k] * matrix2[k][j]
# print the result
    print(result)
    return [[0, 0], [0, 0]]
# create two lists for the matrices W and Z
matrix1 = [[1,2,3],
    [4,5,6],
    [7,8,9]]
matrix2 = [[9,8,7],
    [6,5,4],
    [3,2,1]]
# create a result matrix with zeros initially
result = [[0,0,0],
               [0,0,0],
               [0,0,0]]
# calculate each element of the result matrix 
# the i and j for loops are used to go element by element
# the k for loop is used to calculate the product to be stored at each position in the result.
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):  
       for k in range(len(matrix1)):
           result[i][j] += matrix1[i][k] * matrix2[k][j]

# print the result
print(result)