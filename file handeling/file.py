
#---------- reading the file-----------------

f = open('text_file.txt', 'r')
#       file            mode for reading, a=appending to add content, w=for writing file

content=f.read() #all the content in text file variable is taken by .read() function and store in content variable
print(content) # prints all data in file
f.close()

#-------------writing the file----------
a=open('write.txt','w')
content=a.write("this is the file i want to write")
a.close
a=open('write.txt','r')
containt=a.read()
print(containt)
a.close()
#-------------append the file----------
b=open('write.txt','a')
b.write(" its new content")
b.close()
b=open('write.txt','r')
containt=b.read()
print(containt)
b.close()



