list=[9,8,7,655,6,4,55,43,5]
index=0
for num in list:
    print(num)
    if index==3:
        print("it is waht you are looking for")
    index +=1
print("---------------------------------------------------------")
# it is complex way to print statement after perticuler index in list
# we can make it easy by using Enumerate Function in Python

for index,num in enumerate(list):
    print(num)
    if index==3:
        print("it is waht you are looking for")

# by using enumerate function you can get easyly index value of list
 