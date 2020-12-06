import itertools
with open("inputData.txt") as f:   #inputData.txt is our puzzle input.
    test = f.read()
data = list(map(int,test.split()))
def sol2(data):
    for x in itertools.combinations(data,3):
        if x[0]+x[1]+x[2] == 2020:
            return (x[0]*x[1]*x[2])

def sol1(data):
    for x in itertools.combinations(data,2):
        if x[0]+x[1] == 2020:
            return(x[0]*x[1])
print("Part 1:",sol1(data))
print("Part 2:",sol2(data))
