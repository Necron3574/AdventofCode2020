with open("inputData.txt") as f:
    data = f.read()
data = data.splitlines()
timestamp = int(data[0])
store = timestamp
bus_list = []
for i in data[1].split(","):
    if i =="x":
        pass
    else:
        bus_list.append(int(i))
flag = 0
bid = 0
while True:
    if flag ==1:
        break
    for id in bus_list:
        if timestamp%id == 0:
            print(timestamp)
            print(id)
            bid = id
            flag =1
            break
    if flag ==0:
        timestamp += 1
print((timestamp-store)*bid)
