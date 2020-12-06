import itertools
def sol1(data):
    ans = 0
    for i in data:
        grp = i.split("\n")
        str = ""
        for indiv in grp:
            str+=indiv
        str = set(list(str))
        ans += len(str)
    return ans

def sol2(data):
    ans = 0
    for i in data:
        grp = i.split("\n")
        setlist = []
        for indiv in grp:
            setlist.append(set(indiv))
        result_set = setlist[0]
        for tset in setlist:
            result_set = result_set.intersection(tset)
        ans += len(result_set)
    return ans

with open("inputData.txt") as f:
    data = f.read()
    data = data.split("\n\n")

print("Part 1:",sol1(data))
print("Part 2:",sol2(data))
