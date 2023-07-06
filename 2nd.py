import sys

##Number of vertices
Z = 8

## i,j,k used in 'for' loop to visit the each node

MIN_PROBABILITY = sys.float_info.min
# MIN_PROBABILITY = 0 to store the minimum probability of particular node

##vertices name is given as below
maps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

##Function to count max probability and find the path specific path bewteen two vertices.

def project(graph,direction):
    solve = list(map(lambda i: list(map(lambda j: j, i)), graph))

## map() is used to iterate the variable without explicitly defining the 'for' loop for the each node.
    path = list(map(lambda i: list(map(lambda j: j, i)), direction))

## lambda() can take multiple arguments in a single function without being explicitly called.  
    for k in range(Z):
        for i in range(Z):
            for j in range(Z):     
                if solve[i][j]<solve[i][k] * solve[k][j]:
                    path[i][j] =  path[i][k] + path[k][j][1:]

            
                solve[i][j] = max(solve[i][j], solve[i][k] * solve[k][j])
    maxProb = 0
    ans = ''
    for i in range(Z):
        tmp = 1
        for j in range(Z):
            tmp *= solve[i][j]
        if tmp > maxProb:
            maxProb = tmp
            ans = i
 
    print("Probability:", solve[2][0])
    print("Path:", "->".join(list(path[2][0])))
    print("City:",maps[ans])

#List for storing values for graph and direction
graph = []
direction = []
for i in range(Z):
    tmp = []
    tmp1 = []
    for j in range(Z):
        tmp.append(MIN_PROBABILITY)
        tmp1.append("")
    graph.append(tmp)
    direction.append(tmp1)

#input for 2nd example:
ed=  [[0,1], [1,2], [2,5],[5,4],[4,1], [4,3],[3,0],[3,6],[6,7],[7,4]]
probs= [0.8, 0.6 ,0.8, 0.9, 0.7, 0.8, 0.9, 0.8, 0.9,0.6]



index = 0
for i in ed:
    graph[i[0]][i[1]] = probs[index]
    graph[i[1]][i[0]] = probs[index]
    direction[i[0]][i[1]] = maps[i[0]] + maps[i[1]]
    direction[i[1]][i[0]] = maps[i[1]] + maps[i[0]]
    index += 1

project(graph,direction)
