# You are given a sorted array which is rotated at some random pivot point.

# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

# Example:

# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

# Here is some boilerplate code and test cases to start with:

def rotated_array_search(input_list, number, stin, endin):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if stin > endin:
        print(f"Element {number} not found");
        return -1;                 
                

    mid = (stin + endin) // 2
    midElement = input_list[mid]

    if midElement == number:
        # print(f'{midElement} found using recursion at index {mid}')
        return mid

    if input_list[stin] <= input_list[mid]:
        if number >= input_list[stin] and number <= input_list[mid]:
            return rotated_array_search(input_list, number, stin, mid-1)
        return rotated_array_search(input_list, number, mid+1, endin)    


    if number >= input_list[mid] and number <= input_list[endin]:
        return rotated_array_search(input_list, number, mid+1, endin)
    return rotated_array_search(input_list, number, stin, mid-1)



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    stin = 0
    endin = len(input_list) - 1

    linear_search_output = linear_search(input_list, number)
    rotated_array_search_output = rotated_array_search(input_list, number, stin, endin)


    if linear_search(input_list, number) == rotated_array_search(input_list, number, stin, endin):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])





