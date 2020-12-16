with open("inputData.txt") as f:
    data = f.read()
data = data.splitlines()

def masker1(mask,bstr):
    ans = ""
    for i,j in zip(mask,bstr):
        if i == "X":
            ans += j
        else:
            ans += i
    return int(ans,2)

def masker2(mask,bstr,pos,flag):
    ans = ""
    count = 0
    for i,j in zip(mask,bstr):
        if i == "X":
            if flag == 1:
                ans+=1
                flag =0
            elif count == pos:
                flag = 1
                ans += "0"
            else:
                ans += "0"

        else:
            ans += i
    print(ans)
    return int(ans,2)

def sol1(data):
    mask = ""
    mem = {}
    for i in data:
        if "mask" in i:
            mask = i[7:]
        else:
            temp = i.split(" = ")
            mem_loc = int(str(temp[0])[4:-1])
            mem_val = int(temp[1])
            mem_val = str(bin(mem_val))[2:]
            while len(mem_val)!= len(mask):
                mem_val = "0" + mem_val
            masked_val = masker1(mask,mem_val)
            mem[mem_loc] = masked_val
    ans = 0
    for i in mem.values():
        ans += i
    return ans

def sol2(data):
    discard = "X"
    binstyle = '036b'
    memory = dict()
    default = format(0, binstyle)
    for instruction in data:
        instruction = instruction.strip()
        eq = instruction.find("=") +2
        if "mask" in instruction:
            mask = instruction[eq:]
        else:

            endind = instruction.find("]")
            begind = 4
            memaddr = format(int(instruction[begind:endind]), binstyle)
            operation = int(instruction[eq:])

            memlist = [""]
            for p in range(len(mask)):
                if mask[p] == discard:
                    z = len(memlist)
                    for x in range(0,z):
                        memlist.append(memlist[x]+"1")
                        memlist[x] += "0"
                elif mask[p] == "1":
                    for x in range(len(memlist)): memlist[x] += "1"
                else:
                    for x in range(len(memlist)): memlist[x] += memaddr[p]

            for x in memlist:
                memory[int(x,2)] = operation

    total = 0
    for value in memory:
        total += int(memory[value])
    return total
print("Part 1",sol1(data))
print("Part 2",sol2(data))
