with open("inputData.txt") as f:
    data = f.read()
data = data.splitlines()
def sol1(x):
    SIDlist = []
    for i in x:
        bin = ""
        row = i[0:7]
        for k in row:
            if k=="F":
                bin+="0"
            else:
                bin +="1"
        row = int(bin,2)
        col = i[7:]
        bin = ""
        for k in col:
            if k=="R":
                bin+="1"
            else:
                bin+="0"
        col = int(bin,2)
        SID = row*8+col
        SIDlist.append(SID)
    return sorted(SIDlist)[-1],sorted(SIDlist)
ans1,t = sol1(data)
def sol2(t):
    for i in range(0,len(t)):
        for j in range(0,len(t)):
            if i==j:
                pass
            else:
                if abs(t[i]-t[j])>1 and abs(i-j)==1:
                    return (t[i]+t[j])//2
print("Part 1:",ans1)
print("Part 2:",sol2(t))
