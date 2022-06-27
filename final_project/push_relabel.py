from cmath import inf


# C: the capacity matrix
# source: the index of the source
# sink: the index of the sink

def relabel_to_front(C, source, sink):
 
   # n: number of nodes in the graph
   n = len(C)

   # F: 
   F = [[0] * n for _ in range(n)]
   # residual capacity from u to v is C[u][v] - F[u][v]

   # height of node
   height = [0] * n  

   # flow into node minus flow from node
   excess = [0] * n  

   # neighbours seen since last relabel
   seen   = [0] * n  

   # node "queue" excluding the source node and the sink node
   nodelist = [i for i in range(n) if i != source and i != sink]
 
   def push(u, v):
       # the amount of flow to push -> minimum of excess flow on the node / the leftover forward capacity 
       send = min(excess[u], C[u][v] - F[u][v])

       # increase the foward flow 
       F[u][v] += send

       # decrease the backward flow
       F[v][u] -= send

       # reduce the excess flow at that node
       excess[u] -= send

       # increase the excess flow at the node being pushed with
       excess[v] += send
 
   def relabel(u):
       # Find smallest new height making a push possible,
       # if such a push is possible at all.

       min_height = inf

       
       for v in range(n):
           if C[u][v] - F[u][v] > 0:
               min_height = min(min_height, height[v])
               height[u] = min_height + 1
 
   def discharge(u):
       while excess[u] > 0:
           if seen[u] < n:  # check next neighbour
               v = seen[u]
               if C[u][v] - F[u][v] > 0 and height[u] > height[v]:
                   push(u, v)
               else:
                   seen[u] += 1
           else:  # we have checked all neighbours. must relabel
               relabel(u)
               seen[u] = 0
 
   height[source] = n    # longest path from source to sink is less than n long
   excess[source] = inf  # send as much flow as possible to neighbours of source
   for v in range(n):
       push(source, v)
 
   p = 0
   while p < len(nodelist):
       u = nodelist[p]
       old_height = height[u]
       discharge(u)
       if height[u] > old_height:
           nodelist.insert(0, nodelist.pop(p))  # move to front of list
           p = 0  # start from front of list
       else:
           p += 1

   # for i in range(n):
   #    for j in range(n):
   #       print(F[i][j], ' ', end='')
   #    print("\n")
 
   return sum(F[source])
 
 
# graph = [
#        [0, 16, 13, 0, 0, 0], # testcase
#        [0, 0, 6, 12, 0, 0],
#        [0, 4, 0, 0, 14, 0],
#        [0, 0, 9, 0, 0, 20],
#        [0, 0, 0, 7, 0, 4],
#        [0, 0, 0, 0, 0, 0]]

graph = [
    [0,1000,1000,0],
    [0,0,1,1000],
    [0,0,0,1000],
    [0,0,0,0]
]
 
source = 0; sink = 3
 
print(relabel_to_front(graph, source, sink)) #returns 23