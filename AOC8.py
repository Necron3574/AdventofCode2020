def sol1(instructions):
    acc = 0
    count = 0
    executed_indices = []
    while not count in executed_indices:
        if not count <len(instructions):
            break
        executed_indices.append(count)
        ins,offset=instructions[count].split(" ")
        offset = int(offset)
        if ins == "nop":
            pass
        elif ins == "jmp":
            count += offset-1
        elif ins == "acc":
            acc += offset
        count +=1
    return acc,count

def sol2(instructions):
    for i in range(len(instructions)):
        count = 0
        acc = 0
        ins,offset = instructions[i].split(" ")

        offset = int(offset)
        if ins == "acc":
            continue
        if ins == "jmp":
            changed_ins = "nop"
        else:
            changed_ins = "jmp"
        if offset > 0:
            new_offset = "+" + str(offset)
        else:
            new_offset = str(offset)
        new_instructions = instructions[:i] + [str(changed_ins) + " " +new_offset] + instructions[i+1:]
        acc,check = sol1(new_instructions)
        if check==len(instructions):
            return acc

with open("inputData.txt") as f:
    data = f.read()
    instructions = data.splitlines()

print("Part 1:",sol1(instructions)[0])
print("Part 2:",sol2(instructions))
