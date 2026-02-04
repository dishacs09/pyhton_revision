
#binary search , it has a logn running time 

def binary_search_first_time(arr ,target):
    left = 0
    right = len(arr) -1

    while left <= right :
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target <arr[mid]:
            right =mid -1 
        else :
            left = mid +1

    return target -1 

my_list =[2,3,15,16,20,29,34,67,89,99,101]
target = 2
result = binary_search_first_time(my_list ,target)

if result != 1:
    print(f"element {target}  found at index : {result} ")
else :
    print (f"element {target} not found ")