# Personal re-write of a combination of code from the following:
# http://www.python.org/doc/essays/graphs/
# https://github.com/faif/python-patterns/blob/master/graph_search.py

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def findSinglePath(self, start, end, path = []):
        self.start = start
        self.end = end
        self.path = path
        self.path += [self.start]

        if self.start == self.end:
            return self.path
        if not self.start in self.graph:
            return None

        for node in self.graph[self.start]:
            if node not in self.path:
                newpath = self.findSinglePath(node, self.end, self.path)
                if newpath:
                    return newpath
        return None

    def findAllPaths(self, start, end, path = []):
        self.start = start
        self.end = end
        self.path = path
        self.path += [self.start] # conversion to an array type

        if self.start == self.end:
            return [self.path]
        if not self.start in self.graph:
            return []
        paths = []
        for node in self.graph[self.start]:
            if node not in self.path:
                newpaths = self.findAllPaths(node, self.end, self.path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def findShortestPath(self, start, end, path = []):
        self.start = start
        self.end = end
        self.path = path
        self.path += [self.start]
        if self.start == self.end:
            return self.path
        if not self.start in self.graph:
            return None
        shortestPath = None
        for node in self.graph[self.start]:
            if node not in self.path:
                newpath = self.findShortestPath(node, self.end, self.path)
                if newpath:
                    if not shortestPath or len(newpath) < len(shortestPath):
                        shortestPath = newpath
        return shortestPath

if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    graphOne = Graph(graph)
    #print(graphOne.findSinglePath('A', 'C'))
    #print(graphOne.findAllPaths('A', 'D'))
    print(graphOne.findShortestPath('A', 'C'))
