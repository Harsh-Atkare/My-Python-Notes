f=open('nums.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"the student {i} has {m1} marks in maths")
    print(f"the student {i} has {m2} marks in science")
    print(f"the student {i} has {m3} marks in geo")
    print(line)
    