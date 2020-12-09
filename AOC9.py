import itertools
def sol1(data):
    for i in range(len(data)):
        if i<25:
            continue
        else:
            flag = 0
            comblist = data[i-25:i]
            for x in itertools.combinations(comblist,2):
                if x[0]+x[1] == data[i]:
                    flag = 1
                    break
            if flag != 1:
                return data[i],i
def check(startind):
    count = startind
    sum = 0
    while sum < invalid_num:
        sum += data[count]
        count +=1
    if sum == invalid_num:
        return True
    else:
        return False

def sol2(data):
    invalid_num,ind = sol1(data)
    ans = 0
    for i in range(ind):
        if check(i):
            ans = i
            break
    sum = 0
    big = 0
    smal = 100000000000000000000000000
    while sum != invalid_num:
        if data[ans] > big:
            big = data[ans]
        if data[ans] < smal:
            smal = data[ans]
        sum += data[ans]
        ans += 1
    return big+smal

with open("inputData.txt") as f:
    data = f.read()
    data = list(map(int,data.splitlines()))

print("Part 1",sol1(data)[0])
print("Part 2",sol2(data))
