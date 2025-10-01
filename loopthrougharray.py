nums = [1,2,3,4,5,6]

for i in range(len(nums)):
    print(nums[i])


nums = [10,20,30,40,50]

for i in range(len(nums)):
    print(nums[i])


# or
#without index
for n in nums:
    print(n)   

for i,n in enumerate(nums):
    print(i,n)

nums.reverse()
print(nums)

sortingarr=[84,87,23,45,11,2,90]
print(sortingarr)
sortingarr.sort()
print(sortingarr)

arrname = ["bob","aloce","disha","roja"]
arrname.sort()
print(arrname)

arrname.sort(key=lambda x:len(x))
print(arrname)