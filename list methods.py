l = [6,5,4,3,2,1,33,22,1]
print(l)
l.append(200) #addoing element at last
print(l)
l.sort() #sorting list in assending order
print(l)
l.sort(reverse=True)
print(l) #sorting in decinding order
print(l.index(22)) #22 is on second index position because of we have sort the list in decinding order
print (l.count(1)) #  1 is 2 time in list

print("orignal list is")
print(l)
#making copy of that string
m=l
m[0]=1000
print(l) #here, we made the copy of l list as m, but as we make changes in m list the same changes will automatically made in l list and thats not good practice to do
print(m) 

print(" creating copy of l finction using copy function")
a=l.copy()
a[0]="hmmm... now orignal list inst changing"
print(l)
print(a)

print("now inserting element in list")
l.insert(1,"inserted")
print(l)