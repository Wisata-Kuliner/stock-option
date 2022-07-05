#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber():
    arr = [1,2,3,4,5]
    k = 5
    # Write your code here
    for i in range(len(arr)):
        if arr[i] == k:
            return "YES"
    return "NO"

#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers():
    l = 2
    r = 5
    # Write your code here
    output = []
    for i in range(l, r+1):
        if i % 2 != 0:
            output.append(i)
    return output



if __name__ == "__main__":
    findNumber()