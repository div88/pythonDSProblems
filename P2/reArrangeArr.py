
# # Problem 3: Rearrange Array Digits
# # Rearrange Array Elements
# # Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

# # for e.g. [1, 2, 3, 4, 5]

# # The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

# # Here is some boilerplate code and test cases to start with:

# def rearrange_digits(input_list):
#     """
#     Rearrange Array Elements so as to form two number such that their sum is maximum.

#     Args:
#        input_list(list): Input List
#     Returns:
#        (int),(int): Two maximum sums
#     """
#     pass

def mergeSort(arr):

   if len(arr)>1:
       mid = len(arr)//2
       leftArr = arr[:mid]
       rightArr = arr[mid:]

       #recursion
       mergeSort(leftArr)
       mergeSort(rightArr)

       i=0
       j=0
       k=0

       while i < len(leftArr) and j < len(rightArr):
           if leftArr[i] > rightArr[j]:
               arr[k]=leftArr[i]
               i=i+1
           else:
               arr[k]=rightArr[j]
               j=j+1
           k=k+1

       while i < len(leftArr):
           arr[k]=leftArr[i]
           i=i+1
           k=k+1

       while j < len(rightArr):
           arr[k]=rightArr[j]
           j=j+1
           k=k+1

def rearrange_digits(arr):
    mergeSort(arr)
    print(arr)

    result = []
    arr1 = []
    arr2 = []

    for i in range(len(arr)):
        if i % 2 == 0:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])   

  
    result.append(''.join(map(str, arr1)))
    result.append(''.join(map(str, arr2)))


    
    
    result = list(map(int,result))
    print(result)
    return result;

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 1, 0, 1, 0, 1], [110, 110]])

