#Required Libraries
import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# A function that prints the MST stored
	def printMST(self, parent):
		print ("Edge \tWeight")
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])

	# A function to find the vertex with minimum weight, from the set of vertices
	# not yet included in the mst
	def minKey(self, key, mstSet):

		# Initialize min value
		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

	# Function to create and print MST for a graph
	def primMST(self):

		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		# Setting key to 6 so that the algorithm starts from the 6th vertice
		key[6] = 6
		mstSet = [False] * self.V

		# Setting First node as the root
    #parent[0] = -1

		for cout in range(self.V):

			# Pick the minimum distance vertex from the set of vertices not yet added to the mst.
			u = self.minKey(key, mstSet)

			# Puting the minimum distance vertex in the shortest path tree
			mstSet[u] = True

			# Updating dist value of the adjacent vertices of the picked vertex only if the current
			# distance is greater than new distance and the vertex in not in the shortest path tree
			for v in range(self.V):

				# Updating the key only if graph[u][v] is smaller than key[v]
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u

		self.printMST(parent)

#Defining the size of the graph
g = Graph(7)
#Creating the graph for the algorithm to find the MST
g.graph = [ [0, 28, 0, 0, 0, 10, 0],
			      [28, 0, 16, 0, 0, 0, 14],
			      [0, 16, 0, 12, 0, 0, 0],
			      [0, 0, 12, 0, 22, 0, 18],
			      [0, 0, 0, 22, 0, 25, 24],
            [10, 0, 0, 0, 25, 0, 0],
            [0, 14, 0, 18, 24, 0, 0]]

#Calling the Graph Class for the algorithm to run
g.primMST();

#NOTE:
#SOURCE GEEKSFORGEEKS https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
