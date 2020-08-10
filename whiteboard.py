# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# create function 
# takes in that object 
# ill create a table 
# one key would be for int
# another for strings
# and then would loop through values of each key 
# value is and int i += currently 

test={
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

def sumOfObject(object):
    endSum = 0
    for i in object.values():
        if type(i) is int:
            endSum +=i
    return endSum

print(sumOfObject(test))