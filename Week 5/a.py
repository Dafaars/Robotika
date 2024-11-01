import heapq

def dijkstra(graph, start, goal):
    # Inisialisasi struktur data
    queue = [(0, start, [])]
    seen = set()
    min_distance = {start: 0}

    while queue:
        (cost, current, path) = heapq.heappop(queue)
        
        # Jika sudah mencapai tujuan, kembalikan jalur dan total biayanya
        if current == goal:
            return path + [current], cost
        
        # Jika node sudah dilihat, lewati
        if current in seen:
            continue
        
        seen.add(current)
        path = path + [current]
        
        for neighbor, weight in graph[current].items():
            if neighbor in seen:
                continue
            prev_cost = min_distance.get(neighbor, float('inf'))
            next_cost = cost + weight
            if next_cost < prev_cost:
                min_distance[neighbor] = next_cost
                heapq.heappush(queue, (next_cost, neighbor, path))

    return None, float('inf')

# Contoh graf berbobot
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Penggunaan algoritma Dijkstra
start, goal = 'A', 'D'
path, cost = dijkstra(graph, start, goal)
print(f"Jalur terpendek: {path} dengan biaya total: {cost}")
