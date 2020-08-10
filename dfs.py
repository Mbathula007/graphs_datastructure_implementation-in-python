class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.curr = None
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.curr = self.head
        elif self.head is not None:
            self.curr.next = Node(val)
            self.curr = self.curr.next
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def print_list(self):
        st = ""
        t = self.head
        while True:
            if t is None:
                st = st + str("None")
                break
            else:
                st = st + str(t.val) + str(" --> ")
                t = t.next
        return st

class graph(object):
    def __init__(self, value, gph, parent):
        self.head = value
        self.parent = parent
        self.gph = {value: []}
        self.vertices = [value]
        self.init_time = {}
        self.end_time = {}
        self.time = 0

    def insert(self, value, parent):
        if value not in self.gph:
            self.gph[parent].append(value)
            self.gph[value] = []
            self.vertices.append(value)
        else:
            pass

    def adj(self, node):
        return self.gph[node]

    def bfs(self):
        level_count = 1
        m = self.head
        parent = {m: None}
        level = {m: 0}
        frontier = [m]
        T = [m]
        while True:
            if len(frontier) == 0:
                break
            next = []
            for i in range(len(frontier)):
                for j in self.adj(frontier[i]):
                    if j not in level:
                        level[j] = level_count
                        parent[j] = frontier[i]
                        next.append(j)
                        T.append(j)
            level_count = level_count + 1
            frontier = next
        return level, T
    

    def dfs(self):
        parent = {}
        def DFS_NODE(node,time):
            self.time = self.time + 1
            if node not in self.init_time :
                self.init_time[node] = self.time
            for u in self.adj(node) :
                if u not in parent :
                    parent[u] = node
                    DFS_NODE(u,self.time)
            self.time = self.time + 1
            if node not in self.end_time :
                self.end_time[node] = self.time
        
        for v in self.vertices :
            if v not in parent:
                parent[v] = None
                DFS_NODE(v,self.time)
        return parent,self.end_time,self.init_time

    def topological_sort(self):
        parent = {}
        l = LinkedList()
        def DFS_NODE(node,time):
            self.time = self.time + 1
            if node not in self.init_time :
                self.init_time[node] = self.time
            for u in self.adj(node) :
                if u not in parent :
                    parent[u] = node
                    DFS_NODE(u,self.time)
            l.insert(node)
            self.time = self.time + 1
            if node not in self.end_time :
                self.end_time[node] = self.time
        
        for v in self.vertices :
            if v not in parent:
                parent[v] = None
                DFS_NODE(v,self.time)
        return l.print_list()






x = graph("A", {}, None)
x.insert("B", "A")
x.insert("C", "B")
x.insert("D", "B")
x.insert("E","C")
x.insert("F","D")
print(x.gph)
print(x.vertices)
print(x.bfs())
print(x.dfs())
print(x.topological_sort())