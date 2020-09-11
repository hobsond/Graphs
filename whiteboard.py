import random
mylist= []
myDic = {}
while len(mylist) < 11:
      mylist.append(random.randint(1,11))

check = 0
start = 0 
while start < len(mylist):
  if check == len(mylist):
    check = 0
    start +=1    
  try:
      
    x1 = mylist[start]
    x2 = mylist[check]
    if (start,check) not in myDic or (check,start):
      myDic[(start,check)] = [x1, x2]
    check += 1 
    continue
  except :
    break
print(myDic)