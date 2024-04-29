friend_list ={
    "friend 1":"harsh",
    "friend 2":"amey",
    "friend 3":"kaivalya",
    "friend 4":"raj",
    "friend 5":"rohit"   
}
print(friend_list["friend 3"])

# Dictionaries are ordered collection of elements.
print(friend_list.keys()) # prints keys of dict
for keys in friend_list:
    print(friend_list[keys]) # print value of each key

friend_list2 ={
    "friend 6":"om",
    "friend 7":"adi",
    "friend 8":"domo",
}
print("concadination of two dictionary")
friend_list.update(friend_list2) # adding all data to friend_list, this change in dict in permanent
print(friend_list)
print("clearing the friend_list dict")
friend_list2.clear()
print(friend_list2)
print("removing one item from dict by using pop()")
friend_list.pop("friend 2")
print(friend_list)
print("friend 2 is removed")
