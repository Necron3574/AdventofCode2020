with open("inputData.txt") as f:
    data = f.read()
data = data.splitlines()
ruledic = {}
#Parsing the rules into a dictionary
for i in data:
    temp = i.split(" contain ")
    key = str(temp[0])[:-1]
    val_list = str(temp[1])[:-1].split(", ")
    parsed_val_list = []
    for j in val_list:
        if "1" in j:
            val = str(j)[2:]
        else:
            val = str(j)[2:-1]
        parsed_val_list.append(val)
    ruledic[key] = parsed_val_list
#bag_list is a list of all bags
bag_list = list(ruledic.keys())

target_bag = "shiny gold bag"
#target_list is a list of all bags which indirectly or directly contain the target bag
target_list = [target_bag]
tlen = -1
while len(target_list)!= tlen:
    tlen = len(target_list)
    for bag in bag_list:
        for target in target_list:
            if target != bag:
                if target in ruledic[bag]:
                    target_list.append(bag)
                    break
    target_list = list(set(target_list))
ans = 0
for bag in bag_list:
    if len(set(ruledic[bag]).intersection(set(target_list)))>=1:
        ans +=1
print(ans)
