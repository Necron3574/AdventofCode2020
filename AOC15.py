numlist = [0,13,1,16,6,17]
def solver(numlist,n):
  flag = -1
  for _ in range(n):
      lastnum = numlist[-1]
      flag = 0
      for i in range(len(numlist)-2,-1,-1):
          if numlist[i] == lastnum:
              numlist.append(len(numlist)-i-1)
              flag = 1
              break
      if flag == 0:
          numlist.append(0)
  return numlist[n-1]
print("Part 1",solver(numlist,2020))
print("Part 2",solver(numlist,30000000))
