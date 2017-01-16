class find_shortest_path():

    def __init__(self, inistialState):
        self.matrix = inistialState
        self.start = (0,0)
        self.end = (len(self.matrix)-1, len(self.matrix[0])-1)
        self.shortestPath = []
        self.Path()

    def Path(self):
        try:
            self.ShortestPath(self.end)
        except:
            print "Minimum Steps: 0", "Path: No Valid Path"

    def getBranchStates(self, state):
        rVal = []
        n = len(self.matrix)
        m = len(self.matrix[0])
        idx = state
        offsets = [(-1,0),(0,-1),(0,1),(1,0)]
        for offset in offsets:
            temp =(idx[0] + offset[0], idx[1] + offset[1])
            if temp[0] >= 0 and temp[1] >= 0 and temp[0] < n and temp[1] < m:
                if self.matrix[temp[0]][temp[1]] == 1:
                    pass
                elif self.matrix[temp[0]][temp[1]] == 0:
                    rVal.append(temp)

        return  rVal

    def bfs(self):
        queue = []
        visited = []
        BackTrack = {}
        queue.append(self.start)

        while len(queue) != 0:
            node = queue.pop(0)
            if node == self.end:
                visited.append(node)
                break
            else:
                visited.append(node)
                children = self.getBranchStates(node)
                for child in children:
                    if child not in visited and child not in queue:
                        queue.append(child)
                        BackTrack.setdefault(child, node)

        return BackTrack


    def ShortestPath(self, node):
        backtrack_value = self.bfs()
        path = self.Revers()
        if node == self.start:
            pass
            print "Minimum Steps: %s" %(len(self.shortestPath)-1)
            print "Path: ", path

        else:
            if node == self.end:
                self.shortestPath.append(node)
                new_node = backtrack_value[node]
                self.shortestPath.append(new_node)
                self.ShortestPath(backtrack_value[node])
            else:
                new_node = backtrack_value[node]
                self.shortestPath.append(new_node)
                self.ShortestPath(backtrack_value[node])

    def Revers(self):
        lis = []
        for i in range((len(self.shortestPath)-1),-1,-1):
            lis.append(self.shortestPath[i])
        return lis


matrix = [[0,1,0,1,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,0,0,1,1,0]]
app = find_shortest_path(matrix)
