from collections import defaultdict

isFound = False
allPath = []

class Graph: 

	def __init__(self, vertices): 
		self.V = vertices 
		
		self.graph = defaultdict(list) 

	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	def printAllPathsUtil(self, u, d, visited, path): 

		visited[u]= True
		path.append(str(u)) 

		if u == d:
			global isFound,allPath
			isFound = True
			allPath.append(path.copy())
		else:
			self.graph[u] = sorted(self.graph[u])
			for i in self.graph[u]: 
				if visited[i]== False: 
					self.printAllPathsUtil(i, d, visited, path) 
					
		path.pop() 
		visited[u]= False


	def printAllPaths(self, s, d): 

		visited =[False]*(self.V) 

		path = [] 

		self.printAllPathsUtil(s, d, visited, path) 



inp = input('Enter Input : ').split('/')

s, d = map(int, inp[1].split())

g = Graph(10)
for i in inp[0].split(','):
    a, b = map(int, i.split())
    g.addEdge(a, b)
    g.addEdge(b, a)
g.printAllPaths(s, d) 
if isFound:
	print('All possible path from {} to {} :'.format(s, d))
	for i in sorted(allPath, key=len):
		print(' -> '.join(i))

else:
	print('{} can\'t go to {}'.format(s, d))