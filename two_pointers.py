def two_pointers(nums,target):
    left ,right =0, len(nums) -1

    while left < right:
        current_sum= nums[left]+ nums[right]
        if current_sum == target:
            return True
        
        elif current_sum > target :
            right -= 1
        else :
            left += 1
    return False

mera_list = [2,5,6,8,9,14,17,18,19,22,33,55,59]
target= 29
result = two_pointers(mera_list,target)

#i want to print that th eresulkt is 28 .

if result:
    print(f"target {target} found in the array")
else :
    print(f"target not found in array")
