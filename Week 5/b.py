import heapq
import math

def heuristic(a, b):
    # Menghitung jarak Euclidean antara dua titik
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_star(grid, start, goal):
    # Inisialisasi struktur data
    rows, cols = len(grid), len(grid[0])
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    visited = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            # Mengembalikan jalur jika tujuan tercapai
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        visited.add(current)
        
        # Periksa tetangga (atas, bawah, kiri, kanan)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor in visited and tentative_g_score >= g_score.get(neighbor, float('inf')):
                    continue
                
                if tentative_g_score < g_score.get(neighbor, float('inf')) or neighbor not in [i[1] for i in open_set]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

# Contoh grid (0 = jalan, 1 = rintangan)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Penggunaan algoritma A*
start, goal = (0, 0), (4, 4)
path = a_star(grid, start, goal)
print(f"Jalur A*: {path}")
