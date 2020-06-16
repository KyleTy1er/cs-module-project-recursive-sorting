# TO-DO: Implement a recursive implementation of binary search



def binary_search(arr, target, start, end):
    # base case would be if start does not equal end?
    if end >= start:

        mid = (start + end) // 2

        if target == arr[mid]:
            return mid

        elif arr[mid] > target:
            return binary_search(arr, target, start, mid-1)

        else:
            return binary_search(arr, target, mid + 1, end)

    else:
        # Element is not present in the array
        return -1




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

