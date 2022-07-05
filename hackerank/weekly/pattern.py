import os

# there is a letter pattern, 
# for example, abcd bcd cde dfe, 
# which one of the four data sets has a different pattern?

def pattern():
    # print("test")
    # pattern = "abcd bcd cde fgi" 
    pattern = "abcd bcd cde dfe" 
    data_set = pattern.split(" ")
    same = {}
    same["words"] = {}
    different = {}
    different["words"] = {}
    counter = 0
    for word in data_set:
        # temp = {}
        for i in range(len(word) - 1):
            if counter == 0:
                if word not in same["words"]:
                    same["words"][word] = str(counter)
            # print(word[i], word[i+1])
            # print(ord(word[i]), ord(word[i+1]))
    #         if len(arr) == 0:
                if ord(word[i]) < ord(word[i+1]):
                    same["asc" + str(i) + str(ord(word[i+1]) - ord(word[i]))] = 1
    #                 if "pattern" not in temp and len(temp["pattern"]) == 0:
    #                     temp["pattern"] = ["asc"]
    #                 else:
    #                     temp["pattern"].append("asc")
                elif ord(word[i]) > ord(word[i+1]):
                    same["desc" + str(i) + str(ord(word[i]) - ord(word[i+1]))] = 1
    #                 if "pattern" not in temp and len(temp["pattern"]) == 0:
    #                     temp["pattern"] = ["desc"]
    #                 else:
    #                     temp["pattern"].append("desc")
                else:
                    same["neut" + str(i) + "0"] = 1
    #                 if "pattern" not in temp and len(temp["pattern"]) == 0:
    #                     temp["pattern"] = ["neut"]
    #                 else:
    #                     temp["pattern"].append("neut")
            else:
                if ord(word[i]) < ord(word[i+1]):
                    if "asc" + str(i) + str(ord(word[i+1]) - ord(word[i])) in same:
                        # print(counter, word, same, "asc" + str(i) + str(ord(word[i+1]) - ord(word[i])))
                        same["asc" + str(i) + str(ord(word[i+1]) - ord(word[i]))] += 1
                    else:
                        if "asc" + str(i) + str(ord(word[i+1]) - ord(word[i])) not in different:
                            different["asc" + str(i) + str(ord(word[i+1]) - ord(word[i]))] = 1
                        else:
                            different["asc" + str(i) + str(ord(word[i+1]) - ord(word[i]))] += 1
                        if word not in different["words"]:
                            different["words"][word] = counter
                elif ord(word[i]) > ord(word[i+1]):
                    if "desc" + str(i) + str(ord(word[i]) - ord(word[i+1]))in same:
                        same["desc" + str(i) + str(ord(word[i]) - ord(word[i+1]))] += 1
                    else:
                        if "desc" + str(i) + str(ord(word[i]) - ord(word[i+1])) not in different:
                            different["desc" + str(i) + str(ord(word[i]) - ord(word[i+1]))] = 1
                        else:
                            different["desc" + str(i) + str(ord(word[i]) - ord(word[i+1]))] += 1
                        if word not in different["words"]:
                            different["words"][word] = counter
                else:
                    if "neut" + str(i) + "0" in same:
                        same["neut" + str(i) + "0"] += 1
                    else:
                        if "neut" + str(i) + "0" not in different:
                            different["neut" + str(i) + "0"] = 1
                        else:   
                            different["neut" + str(i) + "0"] += 1
                        if word not in different["words"]:
                            different["words"][word] = counter
    #         else:
        # print(word, different)
        if word not in different["words"]:
            same["words"][word] = counter
        counter += 1
    #             for tmp in arr:
    #                 for pattern in tmp["pattern"]:
    #                     if ord(word[i]) < ord(word[i+1]) and pattern == "asc":
    #                         continue
    #                     if ord(word[i]) < ord(word[i+1]):
    #                         if "pattern" not in temp and len(temp["pattern"]) == 0:
    #                             temp["pattern"] = ["asc"]
    #                         else:
    #                             temp["pattern"].append("asc")
    #                     elif ord(word[i]) > ord(word[i+1]) and pattern != "desc":
    #                         if "pattern" not in temp and len(temp["pattern"]) == 0:
    #                             temp["pattern"] = ["desc"]
    #                         else:
    #                             temp["pattern"].append("desc")
    #                     else:
    #                         if "pattern" not in temp and len(temp["pattern"]) == 0:
    #                             temp["pattern"] = ["neut"]
    #                         else:
    #                             temp["pattern"].append("neut")
    #                 break
    #     if "total" not in temp:
    #         temp["total"] = 1
    #         temp["words"] = [word]
    #     else:
    #         temp["total"] += 1
    #         temp["words"].append(word)
    #     arr.append(temp)
    # for item in arr:
    #     if item["total"] == 1:
    #         print(item["words"])
    for k, v in same.items():
        if len(same["words"]) == 1:
            print("same", same["words"])
    for k, v in different.items():
        if len(different["words"]) == 1:
            # print("different", different["words"])
            print(list(different["words"].keys())[0])
            break

def diagonalDifference():
    arr = [[1,2,3],[4,5,6],[9,8,9]]
    left = 0
    right = 0
    for i in range(len(arr)):
        for j in range(i,len(arr[i]) + 1):
            # print(left, i,j,arr[i][j])
            # print(right, len(arr) - 1 - i, len(arr) - 1 - j, arr[len(arr) - 1 - i][len(arr) - 1 - j])
            left += arr[i][j]
            right += arr[i][len(arr[i]) - 1 - j]
            break
    # print(left, right)
    print(abs(left - right))

def flippingMatrix():
    # matrix = [[1,2],[3,4]] -> 4
    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]] # 414
    division_floor = int(len(matrix)/2)
    total_sub = 0
    for i in range(division_floor):
        for j in range(division_floor):
            maksimum_sub = 0
            if matrix[i][j] > maksimum_sub:
                maksimum_sub = matrix[i][j]
            # max(maximum, matrix[i][j])
            if matrix[i][2*division_floor-j-1] > maksimum_sub:
                maksimum_sub = matrix[i][2*division_floor-j-1]
            # max(maximum , matrix[i][2*n-j-1])
            if matrix[2*division_floor-i-1][j] > maksimum_sub:
                maksimum_sub = matrix[2*division_floor-i-1][j]
            # max(maximum, matrix[2*n-i-1][j])
            if matrix[2*division_floor-i-1][2*division_floor-j-1] > maksimum_sub:
                maksimum_sub = matrix[2*division_floor-i-1][2*division_floor-j-1]
            # max(maximum, matrix[2*n-i-1][2*n-j-1])
            total_sub += maksimum_sub
    print(total_sub)

def findZigZagSequence():
    a = [2,3,5,1,4] # 1,4,5,3,2
    n = 5
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        print(st, ed, a[st], a[ed], a)
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1#1st change
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2#2nd change
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 #3rd change

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

def caesarCipher():
    # Write your code here
    # s = "middle-Outz" # okffng-Qwvb
    # s = "Always-Look-on-the-Bright-Side-of-Life" #Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj
    # s = "Hello_World!" #Lipps_Asvph!
    s = "www.abc.xy" #fff.jkl.gh
    # k = 2
    # k = 5
    # k = 4
    k = 87
    result = ""
    while k > 26:
        k -= 26
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
            print(s[i], ord(s[i]))
            if ord(s[i]) + k > 90 and ord(s[i]) <= 90:
                temp = 64 - 90 + ord(s[i]) + k
            elif ord(s[i]) + k > 122:
                temp = 96 - 122 + ord(s[i]) + k 
            else:
                temp = ord(s[i]) + k
            print(s[i], ord(s[i]), temp)
            result += chr(temp)
        else:
            result += s[i]
    print(result)

def palindromeIndex():
    # s = "aaab"
    # s = "baa"
    s = "aaa"
    if s == s[::-1]:
        return -1
    # Write your code here
    for i in range(len(s)):
        # temp = s.replace(s[i], "")
        # print(temp)
        temp = s[:i] + s[i+1:]
        # print(temp, s[:i], s[i+1:len(s) - i], s[len(s) - i:])
        if temp == temp[::-1]:
            print(i)
    print(-1)

def palindromeIndex(s):
    l = len(s)
    i = 0
    j = l-1
    while i<l:
        if s[i]!=s[j]:
            break
        i+=1
        j-=1
    if i>j: return -1
    a = i+1
    b = j
    while a<j and b>i+1:
        if s[a]!=s[b]:
            return j
        a+=1
        b-=1
    return i

def gridChallenge():
    grid = [['i', 'v'], ['m', 's']] #NO 
    # i v
    # m s
    # Write your code here
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    for i in range(len(grid) - 1):
        for j in range(len(grid[i])):
            # print(grid[i][j], grid[i][j+1], grid[i+1][j])
            if ord(grid[i][j]) > ord(grid[i+1][j]):
                print("NO")
    # print("YES")

def checkLex():
    arr = [['a', 'b', 'c'], ['h', 'j', 'k'], ['m', 'p', 'q'], ['r', 't', 'v']]
    n = 3
    for j in range(n-1):
        for k in range(n):
            print(arr[j][k], j, k)
            if arr[j][k] > arr[j+1][k]:
                print("NO")
    print("YES")

def sort_string(string):
    return "".join(sorted(string))

def sort_string():
    for _ in range(int(input())):
        n = int(input())
        string = []
        for i in range(n):
            s = input()
            string.append(sort_string(s))
        value = True
        for j in range(n):
            for i in range(n-1):
                if string[i][j] > string[i+1][j]:
                    value = False
                    break
            if not value:
                break
        
        if value:
            print('YES')
        else:
            print('NO')

def stillFailed(grid):
    res = 'YES'
    newgrid = []
    
    for row in grid:
        newgrid.append(sorted(row))
        
    #for row in newgrid:
    #    print(row)
        
    for ind in range(len(grid)):
        for jnd in range(ind, len(grid[0])):
            newgrid[ind][jnd], newgrid[jnd][ind] = newgrid[jnd][ind], newgrid[ind][jnd]
            
    for row in newgrid:
        if row != sorted(row):
            res = 'NO'
            break
            
    return res

def superDigit(n, k):
    # Write your code here
    concat = ""
    for i in range(k):
        concat += n
    while len(concat) != 1:
        concat = str(helper(concat))
    return concat
        
def helper(concat):
    digit = 0
    for i in range(len(concat)):
        digit += int(concat[i])
    return digit

def sup_digits(x,k):
    a = digsum(x)
    return sup_digit(str(int(a)*k))

def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit( digsum(x) )

def digsum(x):
    return str(sum((int(i) for i in list(x))))

def minimum_bribes(q):
    q = [i-1 for i in q]  # set queue to start at 0
    bribes = 0
    
    for i, o in enumerate(q):
        cur = i 
        if o - cur > 2:
            print("Too chaotic")
            return
        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)


def minimumBribes():
    q = [2,1,5,3,4]
    # q = [2,5,1,3,4]
    initial = []
    for i in range(len(q)):
        initial.append(i+1)
    bribe = 0
    for i in range(len(q)):
        if abs(q[i] - initial[i]) > 2:
            print("Too chaotic")
            return
        else:
            bribe += 1
    print(bribe)

def petrol():
    a=[]

    for i in range(int(input())):
        a.append(list(map(int, input().split())))
        a[i] = a[i][0] - a[i][1]

    sum = 0
    fin = 0
    shift = 0
    while (fin < len(a)):
        sum+=a[fin]
        if sum < 0:
            for _ in range(fin + 1):
                a.append(a.pop(0))
            sum = 0
            shift += fin + 1
            fin=0
        else:
            fin = fin + 1
                
    print (shift)

def truckTour(petrolpumps):
    # Write your code here
    arr = {}
    minimum = sys.maxsize
    petrol = 0
    for i in range(len(petrolpumps)):
        arr[petrolpumps[i][0]] = petrolpumps[i][1]
        if petrolpumps[i][0] + petrolpumps[i][1] < minimum:
            minimum = petrolpumps[i][0] + petrolpumps[i][1]
            petrol = petrolpumps[i][0]
    return petrol

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def mergeLists(headA, headB):
    if headA == None:
        return headB
    if headB == None:
        return headA
    
    if headA.data <= headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
    
    current = head
    while headA != None or headB != None:
        if headA == None:
            current.next = headB
            break
        if headB == None:
            current.next = headA
            break
        if headA.data <= headB.data:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next
    return head

def isBalanced(s):
    # Write your code here
    if helper(s, 0, 0):
        return "YES"
    return "NO"

def helper(s, i, j):
    if i == len(s):
        return j == 0
    if j < 0:
        return False
    if s[i] == "(" or s[i] == "{" or s[i] == "[":
        return helper(s, i + 1, j + 1)
    elif s[i] == ")" or s[i] == "}" or s[i] == "]":
        return helper(s, i + 1, j - 1)
    return helper(s, i + 1, j)

def isBalance():
    t = int(input())
    while t:
        ar = ['e']
        s = input()
        for i in s:
            if i == '(':
                ar.append('(')
            elif i == '[':
                ar.append('[')
            elif i == '{':
                ar.append('{')
            elif i == ')':
                k = ar.pop()
                if k != '(':
                    ar.append('k')
                    break
            elif i == ']':
                k = ar.pop()
                if k != '[':
                    ar.append('k')
                    break
            elif i == '}':
                k = ar.pop()
                if k != '{':
                    ar.append('k')
                    break
            #print(ar)
        if len(ar) == 0 or ar[len(ar)-1] != 'e':
            print('NO')
        else:
            #print(len(ar), ar[len(ar)-1])
            print('YES')
        t-=1

def pairs():
    k = 2
    arr = [1, 5, 3, 4, 2]
    # Write your code here
    sorted_arr = sorted(arr)
    count = 0
    for i in range(len(sorted_arr)):
        print(sorted_arr[len(sorted_arr)- 1 - i])
        if sorted_arr[len(sorted_arr) - 1 - i] - k in sorted_arr:
            count += 1
    print(count)

def text_editor():
    q = int(input())
    history = []
    s = ""
    for i in range(q):
        ops = input().split(" ")
        temp = {}
        print(s, ops, history)
        if int(ops[0]) == 1:
            s += ops[1]
            temp["cmd"] = 1
            temp["value"] = ops[1]
            history.append(temp)
        elif int(ops[0]) == 2:
            temp["cmd"] = 2
            temp["value"] = s[int(ops[1]):]
            if temp["value"] == "":
                temp["value"] = s[:int(ops[1])]
            history.append(temp)
            tmp = s[:int(ops[1])]
            if tmp == s:
                s = s[int(ops[1]):]
        elif int(ops[0]) == 3:
            print(s[int(ops[1]) - 1])
        else:
            if history[len(history) - 1]["cmd"] == 1:
                s = s[len(history[len(history) - 1]["value"]):]
            elif history[len(history) - 1]["cmd"] == 2:
                s += history[len(history) - 1]["value"]
            del history[len(history) - 1]

def cookies():
    k = 7
    A = [1, 2, 3, 9, 10, 12]  
    # Write your code here
    print(helper(k, A, 0))
    
def helper(k, A, count):
    print(A)
    if len(A) < 2:
        return count
    if A[0] < k:
        count += 1
        temp = 1 * A[0] + 2 * A[1]
        del A[0]
        del A[1]
        A.insert(0, temp)
        return helper(k, A, count)
    else:
        return count   

def bfs(n, m, edges, s):
    nodes = [(i, -1, []) for i in range(1, n+1)]

    for edge in edges:
        start, end = [int(i) for i in edge]
        
        id, cost, edges = nodes[start-1]
        nodes[start-1] = (id, cost, edges + [end])

        id, cost, edges = nodes[end-1]
        nodes[end-1] = (id, cost, edges + [start])

    
    nodes = helper(nodes, [s])

    return [str(node[1]) for node in nodes if node[1] != 0]

def helper(nodes, travel_edges):
    # Write your code here
    new_edges = []
    weight = 6
    current_cost = 0
    
    while travel_edges:
        for e in travel_edges:
            id, cost, edges = nodes[e-1]
            
            if cost == -1:
                new_edges = new_edges + edges
                cost = current_cost
                nodes[e-1] = (id, cost, edges)
            
        travel_edges = new_edges
        new_edges = []
        current_cost += weight
                
    return nodes     

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    result = str(root.info)
    while root.right != None:
        if root.left != None:
            root = root.left
            result += str(root.info)
        else:
            root = root.right
            result += str(root.info)
        result += " "
    print(result)

def noPrefix(words):
    # Write your code here
    sorted_arr = words
    flag = True
    temp = ""
    idx = len(words)
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if sorted_arr[i] in sorted_arr[j]:
                flag = False
                # print(j, idx, sorted_arr)
                if j < idx:
                    idx = j
                    temp = sorted_arr[j]
    if flag:
        print("GOOD SET")
    else:
        print("BAD SET")
        print(temp)

if __name__ == "__main__":
    # choice = input("Welcome to Python Hackerank\n 1. Weird Word Pattern\n 2. Nested Array\n 3. Sub Nested Array\n 4. Highest Middle Array\n 5. Append ord character\n Your input: ")
    # switcher = {
    #     1: pattern()
    #     2: diagonalDifference()
    #     3: flippingMatrix()

    # }
    # palindromeIndex()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     grid = []

    #     for _ in range(n):
    #         grid_item = input()
    #         grid.append(grid_item)

    #     result = gridChallenge(grid)
    #     if t_itr == 79:
    #         print(grid)
        # print(result)

        # fptr.write(result + '\n')

    # fptr.close()
    # gridChallenge()
    # checkLex()
    # first_multiple_input = input().rstrip().split()

    # n = first_multiple_input[0]

    # k = int(first_multiple_input[1])

    # result = superDigit(n, k)
    # print(result)
    # pairs()
    # text_editor()
    # cookies()
    # q = int(input().strip())

    # for q_itr in range(q):
    #     first_multiple_input = input().rstrip().split()

    #     n = int(first_multiple_input[0])

    #     m = int(first_multiple_input[1])

    #     edges = []

    #     for _ in range(m):
    #         edges.append(list(map(int, input().rstrip().split())))

    #     s = int(input().strip())

    #     result = bfs(n, m, edges, s)
    #     print(' '.join(map(str, result)))
    # n = int(input().strip())

    # words = []

    # for _ in range(n):
    #     words_item = input()
    #     words.append(words_item)

    # noPrefix(words)
    pattern()