with open("..\inputData.txt") as f:
    data = f.read()
data = data.splitlines()
store = data
def check(data,x,i,j):
    if x == "L":
            if data[i-1][j-1] == "#":
                if(i-1>=0) and (j-1)>=0:
                    return False
            if data[i-1][j] == "#":
                if(i-1>=0) and (j)>=0:
                    return False
            if data[i][j-1] == "#":
                if (j-1)>=0:
                    return False
            try:
                if data[i-1][j+1] == "#":
                    if(i-1>=0) and (j+1)<len(data[i]):
                        return False
                if data[i][j+1] == "#":
                    if (j+1)<len(data[i]):
                        return False
            except:
                pass
            try:
                if data[i+1][j-1] == "#":
                    if(i+1< len(data[0])) and (j-1)>=0:
                        return False

                if data[i+1][j] == "#":
                    if(i+1< len(data[0])):
                        return False
                if data[i+1][j+1] == "#":
                    if(i+1< len(data[0])) and j+1<len(data[0]):
                        return False
            except:
                pass
            return True

    elif x == "#":
        count =0
        if data[i-1][j-1] == "#":
            if(i-1>=0) and (j-1)>=0:
                count +=1
        if data[i-1][j] == "#":
            if(i-1>=0) and (j)>=0:
                count +=1
        if data[i][j-1] == "#":
            if (j-1)>=0:
                count +=1
        try:
            if data[i-1][j+1] == "#":
                if(i-1>=0) and (j+1)<len(data[i]):
                    count +=1
            if data[i][j+1] == "#":
                if (j+1)<len(data[i]):
                    count +=1
        except:
            pass
        try:
            if data[i+1][j-1] == "#":
                if(i+1< len(data[0])) and (j-1)>=0:
                    count +=1
            if data[i+1][j] == "#":
                if(i+1< len(data[0])):
                    count +=1
            if data[i+1][j+1] == "#":
                if(i+1< len(data[0])) and j+1<len(data[0]):
                    count +=1
        except:
            pass
        if count>=4:
            return True
        return False

def switch1(data,x,i,j):
    if x == ".":
        return x
    if x =="L":
        if(check(data,x,i,j)):
            return "#"
        else:
            return "L"
    if x == "#":
        if(check(data,x,i,j)):
            return "L"
        else:
            return "#"

def switch2(data,x,i,j):
    try:
        k = 1
        while(data[i-k][j-k] == "."):
            k+=1
        if i-k>=0 and j-k>=0:
            lud = data[i-k][j-k]
        else:
            lud = "X"
    except:
        lud = "X"
    try:
        k = 1
        while(data[i-k][j+k] == "."):
            k+=1
        if i-k>=0:
            rud = data[i-k][j+k]
        else:
            rud = "X"
    except:
        rud = "X"
    try:
        k = 1
        while(data[i+k][j-k] == "."):
            k+=1
        if j-k>=0:
            lld = data[i+k][j-k]
        else:
            lld = "X"
    except:
        lld = "X"
    try:
        k = 1
        while(data[i+k][j+k] == "."):
            k+=1
        rld = data[i+k][j+k]
    except:
        rld = "X"
    try:
        k = 1
        while(data[i-k][j] == "."):
            k+=1
        if i-k>=0:
            u = data[i-k][j]
        else:
            u = "X"
    except:
        u = "X"
    try:
        k = 1
        while(data[i][j+k] == "."):
            k+=1
        r = data[i][j+k]
    except:
        r = "X"
    try:
        k = 1
        while(data[i+k][j] == "."):
            k+=1
        down = data[i+k][j]
    except:
        down = "X"
    try:
        k = 1
        while(data[i][j-k] == "."):
            k+=1
        if j-k>=0:
            left = data[i][j-k]
        else:
            left = "X"
    except:
        left = "X"
    temp_list = [u,rud,r,rld,down,lld,left,lud]
    if x == ".":
        return x
    elif x == "L":
        for temp in temp_list:
            if temp == "#":
                return "L"
        return "#"
    elif x == "#":
        count = 0
        for temp in temp_list:
            if temp=="#":
                count += 1
        if count>=5:
            return "L"
        else:
            return "#"

def round(data,solve):
    new_data = []

    for i in range(len(data)):
        temp = ""
        for j in range(len(data[i])):
            if solve ==1:
                temp += switch1(data,data[i][j],i,j)
            elif solve ==2:
                temp += switch2(data,data[i][j],i,j)
        new_data.append(temp)
    return new_data

for _ in range(1000):
    x = round(data,1)
    if x == data:
        break
    data = x
ans = 0
for i in data:
    for j in i:
        if j == "#":
            ans+=1
print("Part 1",ans)
data = store
for _ in range(1000):
    x = round(data,2)
    if x == data:
        break
    data = x
ans = 0
for i in data:
    for j in i:
        if j == "#":
            ans+=1
print("Part 2",ans)
