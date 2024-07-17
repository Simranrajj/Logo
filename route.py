def find_route(tickets, start):
    from collections import defaultdict, deque
    
    # Create a graph from tickets
    graph = defaultdict(list)
    for src, dst in tickets:
        graph[src].append(dst)

    # Sort the destinations to ensure lexical order traversal
    for src in graph:
        graph[src].sort()

    # This will store the final route
    route = []

    # Use DFS to find the route
    def dfs(city):
        while graph[city]:
            next_city = graph[city].pop(0)  # Get the next destination
            dfs(next_city)
        route.append(city)
    
    # Start DFS from the starting city
    dfs(start)
    
    # The route will be in reverse order so reverse it before returning
    return route[::-1]

# List of available tickets
tickets = [
    ("Paris", "Skopje"),
    ("Zurich", "Amsterdam"),
    ("Prague", "Zurich"),
    ("Barcelona", "Berlin"),
    ("Kiev", "Prague"),
    ("Skopje", "Paris"),
    ("Amsterdam", "Barcelona"),
    ("Berlin", "Kiev"),
    ("Berlin", "Amsterdam")
]

# Starting city
start_city = "Kiev"

# Find the route
route = find_route(tickets, start_city)
print("Route:", route)
