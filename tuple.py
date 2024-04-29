tup=(3,2,4,2,5,1)
print(tup)
#tup[1]=32
print(tup[2])

# tuples are unchangable, means we cant add remove or change element in tuple. to change the tuple we have to change it into list then we can oerfirm operation no it
print("converting touple into list and making changes")
temp=list(tup)
print(temp)
print(" the tuple is successfully converted into list")
print("_________________________________________________")

temp.append("harsh")
print(temp)
temp[2]="added"
print(temp)
print("again converting list in tuple")
tup=tuple(temp)
print(tup)