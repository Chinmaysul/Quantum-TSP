# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
import random
from time import *
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s,V):

	# store all vertex apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# store minimum weight Hamiltonian Cycle
	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost)
		current_pathweight = 0

		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)
		
	return min_path


# Driver Code
v=int(input("Number of vertices:")) 
e=int(input("Number of edges:"))
graph = [[maxsize for column in range(v)]
                for row in range(v)]
# matrix representation of graph
i=0
while i<e:
	a,b,c=list(map(int,input().split()))
	if graph[a][b]==maxsize:
		graph[a][b]=c
		graph[b][a]=c
		i+=1
	else:
		continue
    # a=random.randint(0,v-1)
    # b=random.randint(0,v-1)
    # while(b==a):
        # b=random.randint(0,v-1)
    # c=random.randint(1,10)
	
    
st=time()
print(travellingSalesmanProblem(graph,0,v))
et=time()
print(et-st)