# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a, b = 0, 0
    #traverse both pointers through their respective lists
    for i in range(len(merged_arr)):
        # check if pointer is out of bounds of its respective aray
        # if it is, then we just need to copy every element from the other array
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # both indices are still in bounds of their respective arrays
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
        # compare the values at both pointers
        # whichever value is smaller, we copy that value to our merged list
        # increment that pointer

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # phase 1: keep splitting our arr until we have lists of length 1
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2]) 
        right = merge_sort(arr[len(arr) // 2 :])
    # phase 2: building those lists make up by using our 'merge' function
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    while start < mid and start2 < end:

        # what if start < start 2?
        if arr[start] < arr[start2]:
            start += 1

        else: 
            value = arr[start2]
            idx = start2

            while idx != start:

                arr[idx] = arr[idx -1]
                idx -=1

            arr[start] = value

            start += 1
            start2 += 1
            mid += 1


        

def merge_sort_in_place(arr, l, r):
    # Your code here
    if r < l:
        return arr
    else:
        # find middle
        middle = (r - l) // 2
        # recurse on left and right halves
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)

        merge_in_place(arr, l, middle, r)
    return arr

    
