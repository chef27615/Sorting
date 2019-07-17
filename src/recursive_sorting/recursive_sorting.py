# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
    merged_arr =[]
    while len(arrA) and len(arrB):
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
                                                                 
    return merged_arr + arrA + arrB


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[0:mid]
        right = arr[mid:]
        arr = merge_sort(left) + merge_sort(right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
