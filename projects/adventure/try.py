def getDouble(nums):
    key = {}
    for i in nums:
        if i not in key:
            key[i] = 0
        key[i] +=1
    for x in key.items():
        if x[1] == 1:
            return x[0]

t = [1,4,1,56,11,56,4,11,3,6,11,3]

print(getDouble(t))