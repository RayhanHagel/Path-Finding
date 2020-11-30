# Hageru-Ray

GRAPH = {}

GRAPH['Start'] = {}
GRAPH['Start']['A'] = 7
GRAPH['Start']['B'] = 3

GRAPH['A'] = {} 
GRAPH['A']['C'] = 5
GRAPH['A']['D'] = 4

GRAPH['B'] = {}
GRAPH['B']['C'] = 1
GRAPH['B']['E'] = 5

GRAPH['C'] = {}
GRAPH['C']['F'] = 2

GRAPH['D'] = {}
GRAPH['D']['F'] = 4
GRAPH['D']['G'] = 5

GRAPH['E'] = {}
GRAPH['E']['H'] = 1

GRAPH['F'] = {}
GRAPH['F']['E'] = 7
GRAPH['F']['H'] = 9
GRAPH['F']['G'] = 2

GRAPH['G'] = {}
GRAPH['G']['End'] = 3

GRAPH['H'] = {}
GRAPH['H']['End'] = 2

GRAPH['End'] = {}


class Algorithm:
    def __init__(self):
        self.infinite = float('inf')
        self.start = 'Start'
        self.end = 'End'
        self.costs = {}
        self.parent = {}
    
        self.graph = GRAPH        
        
    def route(self, costs, is_checked):
        fast_node = None
        lowest_cost = self.infinite
        for node in is_checked:
            if costs[node] <= lowest_cost:
                lowest_cost = costs[node]
                fast_node = node
        return fast_node

    def brain(self):
        for node in self.graph:
            self.costs[node] = self.infinite
            self.parent[node] = {}

        self.costs[self.start] = 0
        
        check_queue = [x for x in self.costs]
        node = self.route(self.costs, check_queue)
        
        while check_queue:
            current_cost = self.costs[node]
            next_cost = self.graph[node]
        
            for amount in next_cost:
                if self.costs[amount] > current_cost + next_cost[amount]:
                    self.costs[amount] = current_cost + next_cost[amount]
                    self.parent[amount] = node
        
            check_queue.pop(check_queue.index(node))
            node = self.route(self.costs, check_queue)

dijktra = Algorithm()
            
            
if __name__ == "__main__":
    dijktra.brain()
    
    if dijktra.costs[dijktra.end] < dijktra.infinite:
        route = [dijktra.end]
        var = 0
        while dijktra.start not in route:
            route.append(dijktra.parent[route[var]])
            var += 1
        
        print(f"The cost from '{dijktra.start}' to '{dijktra.end}' is {dijktra.costs[dijktra.end]}")
        print(f'Fastest route is {route[::-1]}')
        
    else:
        print(f'Invalid route')