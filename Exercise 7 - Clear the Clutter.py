import os
#os.rename("images/temp.txt", "images/changed.txt")

# putiing all file of images folder in single veriable "file"
files=os.listdir("images")
print(type(files))
#by using for loop, print all files in files(veriable)
i=1
for file in files:
    print(file)
    #only .png file will print
    if file.endswith(".png"):
        print(file) 
        os.rename(f"images/{file}", f"images/{i}.png")
        i+=1