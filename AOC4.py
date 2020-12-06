with open("inputData.txt", "r") as f:
    data =(f.read())
data = data.split("\n\n")

def check1(str):
    pass
def check2(str):
    temp =str.split()
    temp = sorted(temp)
    field = 0
    for i in temp:
        if "byr" in i:
            field +=1
            byr = i.split(":")[1]
            if len(byr) != 4:
                # print("byr error")
                return False
            byr = int(byr)
            if byr < 1920 or byr > 2002:
                # print("byr error")
                return False
        if "iyr" in i:
            field +=1
            iyr = i.split(":")[1]
            if len(iyr) != 4:
                # print("iyr error")
                return False
            iyr = int(iyr)
            if iyr < 2010 or iyr > 2020:
                # print("iyr error")
                return False
        if "eyr" in i :
            field +=1
            eyr = i.split(":")[1]
            if len(eyr) != 4:
                # print("eyr error")
                return False
            eyr = int(eyr)
            if eyr < 2010 or eyr > 2030:
                # print("eyr error")
                return False
        if "hgt" in i:
            field +=1
            hgt = i.split(":")[1]
            # print(hgt)
            if "cm" in i:
                hgt = int(hgt[:-2])
                if hgt<150 or hgt>193:
                    # print("hgt error")
                    return False
            elif "in" in i:
                hgt = int(hgt[:-2])
                if hgt<59 or hgt>76:
                    # print("hgt error")
                    return False
            else:
                return False
        if "hcl" in i:
            field +=1
            hcl = i.split(":")[1]
            if hcl[0] != "#":
                # print("hcl error")
                return False
            if len(hcl) != 7:
                # print("hcl error")
                return False
            acceptable = "0123456789abcdef"
            new_hcl = hcl[1:]
            for k in new_hcl:
                if not k in acceptable:
                    print(hcl)
                    return False
        if "ecl" in i:
            field +=1
            ecl = i.split(":")[1]
            acceptable = ['amb' ,'blu' ,'brn' ,'gry' ,'grn' ,'hzl','oth']
            if not ecl in acceptable:
                # print("ecl error")
                return False
        if "pid" in i:
            field +=1
            pid = i.split(":")[1]
            if not len(pid)==9:
                # print("pid error")
                return False
    if field >= 7:
        return True
    else:
        return False
def sol1(data):
    ans = 0
    for x in data:
        if len(x.split())==8:
            ans+=1
        elif len(x.split())==7:
            if "cid" in x:
                continue
            else:
                ans+=1
        else:
            continue
    return ans
def sol2(data):
    ans = -1
    for x in data:
        if len(x) ==0:
            continue
        if check2(x):
            ans+=1
    return ans
print("Part 1:",sol1(data))
print("Part 2:",sol2(data))
