a={2,1,4,3,2,1}
print(a)
#in output you can see, sets dont contain reperated element (do not cantain duplicate item)
#sets are unordered means the element can print randomly
# because sets are unordered thatswhy you cant access element by using a[1] index
#print(a[2])

#finding union within two sets
a1={1,2,3,4,5,6,7}
a2={4,3,11,66,44,33,2}
print(a1,a2)
#print(a1.union(a2))
#print(a1.intersection(a2))
#a1.update(a2) #  update() will add every element inside a1 which is present in a2
print(a1)
print(a1.symmetric_difference(a2)) #all values in a1 and a2 except common values
print(a1.difference(a2)) # all in a1 except these which are also present inn a2
print(a1.isdisjoint(a2)) #this function prints bool values which indigats does a1 and a2 has common vlues? is no then false,if yes the true
b1={1,2,3,4,5,6,7}
b2={3,4,5}
print(b1.issuperset(b2)) # is all element of a2 is present in a1? if yes then true,if no then false
print(b1.issubset(b2)) # this function is exact opposite of superset

del a1 # del use to delete entire set