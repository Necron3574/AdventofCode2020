import itertools
def checkfreq(target,str):
    count = 0
    for i in str:
        if target == i:
            count +=1
    return count
with open("inputData.txt") as f:       #inputData.txt is our puzzle input
    test = f.read()
data = test.splitlines()

def sol1(data):
    ans = 0
    for x in data:
        vars = x.split()
        temp = vars[0].split("-")
        mini = int(temp[0])
        maxi = int(temp[1])
        target = vars[1].split(":")[0]
        str = vars[2]
        num = checkfreq(target,str)
        if num <mini or num>maxi:
            ans +=1
    return ans

def sol2(data):
    ans = 0
    for x in data:
        flag = 0
        vars = x.split()
        temp = vars[0].split("-")
        pos1 = int(temp[0])-1
        pos2 = int(temp[1])-1
        target = vars[1].split(":")[0]
        str = vars[2]
        if str[pos1] == target:
            flag +=1
        if str[pos2] == target:
            flag +=1
        if flag==1:
            ans+=1
    return ans

print("Part 1:",sol1(data))
print("Part 2:",sol2(data))
