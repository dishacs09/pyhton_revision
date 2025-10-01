mySet=set()

mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(2)  # Duplicate, will not be 

print(mySet)

#check if a element is present in hashset or not 


print(2 in mySet)
print(678 in mySet)

#remove a value from hashset 

mySet.remove(2)
print(mySet)
#above line will show the items in set
#below line will confirm if its removed by giving false 
print(2 in mySet)