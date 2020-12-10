import itertools
with open("inputData.txt") as f:
    data = f.read()
data = [0] + sorted(list(map(int,data.splitlines())))
def sol1(data):
    diff1 = 1
    diff3 = 1
    for i,j in zip(range(0,len(data)-1),range(1,len(data))) :
        if data[j]-data[i] == 1:
            if (data[i]==0) or data[j]==52:
                continue
            diff1+=1
        elif data[j]-data[i] == 3:
            if (data[i]==0) or data[j]==52:
                continue
            diff3 +=1
    return(diff1*diff3)

def sol2(data):
    mydict = {}
    for i in data:
        if i == 0:
            mydict[i] = 1
            continue
        temp = 0
        for j in range(i-3, i):
            if j in data:
                temp += mydict[j]
        mydict[i] = temp

    return(mydict.get(data[-1]))
print("Part 1",sol1(data))
print("Part 2",sol2(data))
