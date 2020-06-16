
# TO-DO: complete the helper function below to merge 2 sorted arrays

# how to merge two sorted arrays?
# how to tell which array goes first?
        # The last element should tell the order?
        # should always be able to compare with list[-1]


def merge(arrA, arrB):
    # stores the length of both arrays in an int value:
    elements = len(arrA) + len(arrB)
    # creates an array of zeros the exact length of our combined arrays.
    merged_arr = [0] * elements

    # main iterator
    m_i = 0
    # left iterator
    l_i = 0
    # right iterator
    r_i = 0

    # while left iterator is less than length of left array AND
    # while right iterator is less than length of right array
    while (l_i < len(arrA)) and (r_i < len(arrB)):

        # if right array value at this iteration is less than left array value
        # update the merged array of this iteration location with main iterator value
        # and update the left iterator value for the next pass
        if arrA[l_i] <= arrB[r_i]:
            merged_arr[m_i] = arrA[l_i]
            l_i += 1

        # if not less than or equal to, do the reverse and store the right iterator value
        # in the iterator value of m_i
        else:
            merged_arr[m_i] = arrB[r_i]
            r_i += 1

        # after each of the above passes update the main iterator value:
        m_i += 1

    # while left iterator is less than length of left array but right iterator is not:
    # meaning the right array has been appended and the left has remaining values:
    # store the sorted values each pass into merged_arr
    while (l_i < len(arrA)):
        merged_arr[m_i] = arrA[l_i]
        l_i += 1
        m_i += 1

    # reverse of the above to account for expenditure of left array:
    while (r_i < len(arrB)):
        merged_arr[m_i] = arrB[r_i]
        r_i += 1
        m_i += 1

    return merged_arr

# # TO-DO: implement the Merge Sort function below recursively
# what is the base case/terminating case?

def merge_sort(arr):
    # base case is if the length of the array is less than 1
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge(left, right)

    return arr

