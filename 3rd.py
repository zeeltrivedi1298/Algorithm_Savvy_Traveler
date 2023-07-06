import sys

#Number of vertices
Z = 8
## i,j,k used in'for' loop to visit the each node

MIN_PROBABILITY = sys.float_info.min
# MIN_PROBABILITY = 0  to store the minimum probability of particular node

#vertices name is given as below
maps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#Function to count max probability and find the path specific path bewteen two vertices.
def project(graph,direction):
    solve = list(map(lambda i: list(map(lambda j: j, i)), graph))
    ## map() is used to iterate the variable without explicitly defining the 'for' loop for each node.
    path = list(map(lambda i: list(map(lambda j: j, i)), direction))
    ## lambda() can take multiple arguments in a single function without being explicitly called.
    
    for k in range(Z):
        for i in range(Z):
            for j in range(Z):     
                if solve[i][j]<solve[i][k] * solve[k][j]:
                    path[i][j] =  path[i][k] + path[k][j][1:]
        ## to select the maximum distance between the two nodes(vertices).
        ## For example, probability of A to  B is 10; probability of A to C is 7 and C to B is 5, then it will return the probabilty of A to B = 35.
            
                solve[i][j] = max(solve[i][j], solve[i][k] * solve[k][j])
    ## to find the maximum probability of city
    maxProb = 0 ##initializing the maximum probabiltiy to 0
    ans = ''    ##  to store the final answer and it initialized as NULL
    for i in range(Z):
        tmp = 1
        for j in range(Z):
            tmp *= solve[i][j] ## calling solve() to find the maximum probability and store that value in tmp*
        if tmp > maxProb:  ## compare tmp* with maxProb, and print the maximum
            maxProb = tmp  ## select the path which has the maximum the value.
            ans = i
 
    print("Probability:", solve[4][2])
    print("Path:", "->".join(list(path[4][2])))
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

#input for 3rd example:
ed= [[0,1],[1,2],[2,3],[3,0],[0,4],[4,5],[5,6],[6,7],[7,4],[7,3],[6,2],[5,1]]
probs=  [0.8,0.6,0.9,0.9,0.8,0.6,0.9,0.6,0.8,0.7,0.6,0.7]




index = 0
for i in ed:
    graph[i[0]][i[1]] = probs[index]
    graph[i[1]][i[0]] = probs[index]
    direction[i[0]][i[1]] = maps[i[0]] + maps[i[1]]
    direction[i[1]][i[0]] = maps[i[1]] + maps[i[0]]
    index += 1

project(graph,direction)
