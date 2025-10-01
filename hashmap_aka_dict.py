#initializing a hashap
myhashmap={}
myhashmap["disha"]=100
myhashmap["abc"]=300
myhashmap["xyz"]=890

print(myhashmap)
print(len(myhashmap))

#assign a diff value to a key
myhashmap["disha"]=500
print(myhashmap)

#pop any key value in hashmap
myhashmap.pop("disha")
print(myhashmap)

#cheeck if a key is present in hashmap or not ,same as other 
print("disha" in myhashmap)

#printint a dict using a loop
hashmap2={i :1*4 for i in range(8)}
print(hashmap2)

