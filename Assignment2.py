# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    numbers=list(set(numbers))
    numbers.sort()
    return numbers
numbers=[]
print(remove_duplicates_and_sort(numbers))

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result=[]
    total=0
    for num in arr:
        total += num
        result.append(total)
    return result
arr=[]
print(cumulative_sum(arr))

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    output = []
    for i in range(len(lst)):
        if i % step == 0:
            output.append(lst[i])
    return output
lst=[]
step=1
print(slice_every_nth(lst, step))
# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    multiply_list = [a*b for a, b in zip(list1, list2)]
    dot_product_list = sum(multiply_list)
    return dot_product_list
list1=[]
list2=[]
print(dot_product(list1, list2))
# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    
    return [[0, 0], [0, 0]]
