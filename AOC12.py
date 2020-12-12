import math

def displace(ins,val,pos):
    if ins == "N":
        pos[1] += val
    elif ins == "S":
        pos[1] -= val
    elif ins == "E":
        pos[0] += val
    elif ins == "W":
        pos[0] -= val

def rotate(ins,val,angle):
    if ins == "L":
        angle = (angle+val)%360
    elif ins == "R":
        angle = (angle-val)%360
    return angle

def move(val,pos,angle):
    x_disp = int(val*math.cos(math.radians(angle)))
    y_disp = int(val*math.sin(math.radians(angle)))
    pos[0] += x_disp
    pos[1] += y_disp

def waypoint_displace(ins,val,wpos):
    if ins == "N":
        wpos[1]+=val
    elif ins == "E":
        wpos[0]+=val
    elif ins == "S":
        wpos[1]-=val
    elif ins == "W":
        wpos[0]-=val

def waypoint_rotate(ins,val,wpos):
    if ins == "L":
        rotnum = val//90
        for _ in range(rotnum):
            wpos[0],wpos[1] = -wpos[1],wpos[0]
    if ins == "R":
        rotnum = val//90
        for _ in range(rotnum):
            wpos[0],wpos[1] = wpos[1],-wpos[0]

def waypoint_forward(val,wpos,pos):
    pos[0] = pos[0]+ val*wpos[0]
    pos[1] = pos[1]+ val*wpos[1]

def sol1(data):
    pos = [0,0]
    angle = 0
    for instruction in data:
        ins = instruction[0]
        val = int(instruction[1:])
        if ins in ['N','S','E','W']:
            displace(ins,val,pos)
        elif ins in ['L','R']:
            angle = rotate(ins,val,angle)
        else:
            move(val,pos,angle)
    return(abs(pos[0])+abs(pos[1]))

def sol2(data):
    pos = [0,0]
    angle = 0
    wpos = [10,1]
    for instruction in data:
        ins = instruction[0]
        val = int(instruction[1:])
        if ins in ['N','S','E','W']:
            waypoint_displace(ins,val,wpos)
        elif ins in ['L','R']:
            waypoint_rotate(ins,val,wpos)
        else:
            waypoint_forward(val,wpos,pos)
    return(abs(pos[0])+abs(pos[1]))

with open("../inputData.txt") as f:
    data = f.read()
data = data.splitlines()
print("Part 1:",sol1(data))
print("Part 2:",sol2(data))
